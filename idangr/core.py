from memory import SimSymbolicIdaMemory
from context import load_project, get_memory_type, SIMPROCS_FROM_CLE
from brk import get_linux_brk
from got_builder import build_mixed_got

import angr
import claripy

import idaapi
import idc


def StateShot():
    idc.RefreshDebuggerMemory()
    
    project = load_project()
    
    mem = SimSymbolicIdaMemory(memory_backer=project.loader.memory, permissions_backer=None, memory_id="mem")
    
    state = project.factory.blank_state(plugins={"memory": mem})

    for reg in sorted(project.arch.registers, key=lambda x: project.arch.registers.get(x)[1]):
        if reg in ("sp", "bp", "ip"):
            continue
        try:
            setattr(state.regs, reg, idc.GetRegValue(reg))
        except:
            pass
    
    ## inject code to get brk if we are on linux x86/x86_64
    if project.simos.name == "Linux":
        if project.arch.name in ("AMD64", "X86"):
            state.posix.set_brk(get_linux_brk())

    if get_memory_type() == SIMPROCS_FROM_CLE:
        state = build_mixed_got(projet, state)
    
    return state



class StateManager(object):
    def __init__(self, state=None):
        self.state = StateShot() if state is None else state
        self.symbolics = {}
    
    def sim(self, key, size=None):
        '''
        key: memory address(int) or register name(str)
        size: size of object in bytes
        '''
        project = load_project()
        if key in project.arch.registers:
            if size == None:
                size = project.arch.registers[key][1]
            size *= 8
            s = claripy.BVS("idangr_reg_" + str(key), size)
            setattr(self.state.regs, key, s)
            self.symbolics[key] = (s, size)
        elif type(key) == int or type(key) == long:
            if size == None:
                size = project.arch.bits
            else:
                size *= 8
            s = claripy.BVS("idangr_mem_" + hex(key), size)
            self.state.memory.store(key, s)
            self.symbolics[key] = (s, size)
        elif type(key) == claripy.ast.bv.BV:
            key = self.state.solver.eval(key, cast_to=int)
            self.sim(key, size)
        else:
            raise ValueError("key must be a register name or a memory address, not %s" % str(type(key)))
    
    def sim_from_set(self, simset):
        for key in simset.symbolics:
            if key in load_project().arch.registers:
                setattr(self.state.regs, key, simset.symbolics[key][0])
            else:
                self.state.memory.store(key, simset.symbolics[key][0])
    
    def __getitem__(self, key):
        if key in load_project().arch.registers:
            return getattr(self.state.regs, key)
        elif type(key) == int or type(key) == long:
            return self.state.mem[key]
        elif type(key) == claripy.ast.bv.BV:
            return self.state.mem[key]
        else:
            raise ValueError("key must be a register name or a memory address")
    
    def __setitem__(self, key, value):
        if key in load_project().arch.registers:
            setattr(self.state.regs, key, value)
        elif type(key) == int or type(key) == long or type(key) == claripy.ast.bv.BV:
            self.state.memory[key] = value
        else:
            raise ValueError("key must be a register name or a memory address")
    
    def simulation_manager(self):
        return load_project().factory.simulation_manager(self.state)
    
    def to_dbg(self, found_state):
        if type(found_state) == StateManager:
            return self.to_dbg(found_state.state)
        for key in self.symbolics:
            try:
                if key in load_project().arch.registers:
                    r = found_state.solver.eval(self.symbolics[key][0], cast_to=int)
                    idc.SetRegValue(r, key)
                else:
                    r = found_state.solver.eval(self.symbolics[key][0], cast_to=str)
                    for i in xrange(len(r)):
                        idc.PatchByte(key + i, ord(r[i]))
            except Exception as ee:
                print " >> failed to write %s to debugger" % key
                #print ee
    
    def concretize(self, found_state):
        if type(found_state) == StateManager:
            return self.concretize(found_state.state)
        ret = {}
        for key in self.symbolics:
            try:
                if key in load_project().arch.registers:
                    r = found_state.solver.eval(self.symbolics[key][0], cast_to=int)
                    ret[key] = r
                else:
                    r = found_state.solver.eval(self.symbolics[key][0], cast_to=str)
                    ret[key] = r
            except Exception as ee:
                print " >> failed to concretize %s" % key
                #print ee
        return ret
        








"""
class SimbolicsSet(object):
    '''
    for future use
    '''
    def __init__(self):
        self.symbolics = {}
    
    def add(self, key, size=None):
        '''
        key: memory address(int) or register name(str)
        size: size of object in bytes
        '''
        project = load_project()
        if key in project.arch.registers:
            if size == None:
                size = project.arch.registers[key][1]
            size *= 8
            s = claripy.BVS("idangr_reg_" + str(key), size)
            self.symbolics[key] = (s, size)
        elif type(key) == int or type(key) == long:
            if size == None:
                size = project.arch.bits
            else:
                size *= 8
            s = claripy.BVS("idangr_mem_" + hex(key), size)
            self.symbolics[key] = (s, size)
        elif type(key) == claripy.ast.bv.BV:
            key = self.state.solver.eval(key, cast_to=int)
            self.sim(key, size)
        else:
            raise ValueError("key must be a register name or a memory address, not %s" % str(type(key)))
    
    def remove(self, key):
        if type(key) == claripy.ast.bv.BV:
            key = self.state.solver.eval(key, cast_to=int)
        del self.symbolics[key]
    
    def regs(self):
        for key in self.symbolics:
            if type(key) == str:
                yield key
    
    def mems(self):
        for key in self.symbolics:
            if type(key) != str:
                yield (key, self.symbolics[key][1])
    """

