from typing import Dict, Any
import re

# define some base type aliases so we can keep track of absolute and relative addresses
T_RelativeAddress = int
T_AbsoluteAddress = int

# parser options are just dictionaries with arbitrary values
T_ParserOpts = Dict[str, Any]

NUMBER_SYMBOL_PATTERN = re.compile(r"^\d+[fb]$")

# base classes
from .flags import MemoryFlags
from .int32 import UInt32, Int32
from .float32 import Float32
from .instruction import Instruction, Immediate
from .instruction_context import InstructionContext
from .memory_section import MemorySection
from .program import Program
from .program_loader import ProgramLoader
from .cpu import CPU
from .simple_instruction import SimpleInstruction
from .instruction_memory_section import InstructionMemorySection
from .binary_data_memory_section import BinaryDataMemorySection

# exceptions
from .exceptions import (
    ParseException,
    NumberFormatException,
    MemoryAccessException,
    OutOfMemoryException,
    LinkerException,
    LaunchDebuggerException,
    RiscemuBaseException,
    InvalidRegisterException,
    InvalidAllocationException,
    InvalidSyscallException,
    UnimplementedInstruction,
    INS_NOT_IMPLEMENTED,
)
