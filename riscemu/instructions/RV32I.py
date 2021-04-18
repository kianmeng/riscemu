from .InstructionSet import *

from ..helpers import int_from_bytes, int_to_bytes, to_unsigned, to_signed


class RV32I(InstructionSet):
    def instruction_lb(self, ins: 'LoadedInstruction'):
        rd, addr = self.parse_mem_ins(ins)
        self.regs.set(rd, int_from_bytes(self.mmu.read(addr, 1)))

    def instruction_lh(self, ins: 'LoadedInstruction'):
        rd, addr = self.parse_mem_ins(ins)
        self.regs.set(rd, int_from_bytes(self.mmu.read(addr, 2)))

    def instruction_lw(self, ins: 'LoadedInstruction'):
        rd, addr = self.parse_mem_ins(ins)
        self.regs.set(rd, int_from_bytes(self.mmu.read(addr, 4)))

    def instruction_lbu(self, ins: 'LoadedInstruction'):
        rd, addr = self.parse_mem_ins(ins)
        self.regs.set(rd, int_from_bytes(self.mmu.read(addr, 1), unsigned=True))

    def instruction_lhu(self, ins: 'LoadedInstruction'):
        rd, addr = self.parse_mem_ins(ins)
        self.regs.set(rd, int_from_bytes(self.mmu.read(addr, 2), unsigned=True))

    def instruction_sb(self, ins: 'LoadedInstruction'):
        rd, addr = self.parse_mem_ins(ins)
        self.mmu.write(addr, 1, int_to_bytes(self.regs.get(rd), 1))

    def instruction_sh(self, ins: 'LoadedInstruction'):
        rd, addr = self.parse_mem_ins(ins)
        self.mmu.write(addr, 2, int_to_bytes(self.regs.get(rd), 2))

    def instruction_sw(self, ins: 'LoadedInstruction'):
        rd, addr = self.parse_mem_ins(ins)
        self.mmu.write(addr, 4, int_to_bytes(self.regs.get(rd), 4))

    def instruction_sll(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            to_signed(to_unsigned(self.regs.get(src1)) << (self.regs.get(src2) & 0b11111))
        )

    def instruction_slli(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        imm = ins.get_imm(2)
        self.regs.set(
            dst,
            to_signed(to_unsigned(self.regs.get(src1)) << (imm & 0b11111))
        )

    def instruction_srl(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            to_signed(to_unsigned(self.regs.get(src1)) >> (self.regs.get(src2) & 0b11111))
        )

    def instruction_srli(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        imm = ins.get_imm(2)
        self.regs.set(
            dst,
            to_signed(to_unsigned(self.regs.get(src1)) >> (imm & 0b11111))
        )

    def instruction_sra(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            self.regs.get(src1) >> (self.regs.get(src2) & 0b11111)
        )

    def instruction_srai(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        imm = ins.get_imm(2)
        self.regs.set(
            dst,
            self.regs.get(src1) >> (imm & 0b11111)
        )

    def instruction_add(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            self.regs.get(src1) + self.regs.get(src2)
        )

    def instruction_addi(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        imm = ins.get_imm(2)
        self.regs.set(
            dst,
            self.regs.get(src1) + imm
        )

    def instruction_sub(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            self.regs.get(src1) - self.regs.get(src2)
        )

    def instruction_lui(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 2)
        reg = ins.get_reg(0)
        imm = ins.get_imm(1)
        self.regs.set(reg, imm << 12)

    def instruction_auipc(self, ins: 'LoadedInstruction'):
        INS_NOT_IMPLEMENTED(ins)

    def instruction_xor(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            self.regs.get(src1) ^ self.regs.get(src2)
        )

    def instruction_xori(self, ins: 'LoadedInstruction'):
        INS_NOT_IMPLEMENTED(ins)

    def instruction_or(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            self.regs.get(src1) | self.regs.get(src2)
        )

    def instruction_ori(self, ins: 'LoadedInstruction'):
        INS_NOT_IMPLEMENTED(ins)

    def instruction_and(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            self.regs.get(src1) & self.regs.get(src2)
        )

    def instruction_andi(self, ins: 'LoadedInstruction'):
        INS_NOT_IMPLEMENTED(ins)

    def instruction_slt(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            int(self.regs.get(src1) < self.regs.get(src2))
        )

    def instruction_slti(self, ins: 'LoadedInstruction'):
        INS_NOT_IMPLEMENTED(ins)

    def instruction_sltu(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        dst = ins.get_reg(0)
        src1 = ins.get_reg(1)
        src2 = ins.get_reg(2)
        self.regs.set(
            dst,
            int(to_unsigned(self.regs.get(src1)) < to_unsigned(self.regs.get(src2)))
        )

    def instruction_sltiu(self, ins: 'LoadedInstruction'):
        INS_NOT_IMPLEMENTED(ins)

    def instruction_beq(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        reg1 = ins.get_reg(0)
        reg2 = ins.get_reg(1)
        dest = ins.get_imm(2)
        if self.regs.get(reg1) == self.regs.get(reg2):
            self.pc = dest

    def instruction_bne(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        reg1 = ins.get_reg(0)
        reg2 = ins.get_reg(1)
        dest = ins.get_imm(2)
        if self.regs.get(reg1) != self.regs.get(reg2):
            self.pc = dest

    def instruction_blt(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        reg1 = ins.get_reg(0)
        reg2 = ins.get_reg(1)
        dest = ins.get_imm(2)
        if self.regs.get(reg1) < self.regs.get(reg2):
            self.pc = dest

    def instruction_bge(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        reg1 = self.get_reg(ins, 0)
        reg2 = self.get_reg(ins, 1)
        dest = self.get_reg(ins, 2)
        if reg1 >= reg2:
            self.pc = dest

    def instruction_bltu(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        reg1 = self.get_reg(ins, 0)
        reg2 = self.get_reg(ins, 1)
        dest = ins.get_imm(2)
        if to_unsigned(reg1) < to_unsigned(reg2):
            self.pc = dest

    def instruction_bgeu(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 3)
        reg1 = to_unsigned(self.get_reg(ins, 0))
        reg2 = to_unsigned(self.get_reg(ins, 1))
        dest = ins.get_imm(2)
        if reg1 >= reg2:
            self.pc = dest

    # technically deprecated
    def instruction_j(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 1)
        addr = ins.get_imm(0)
        self.pc = addr

    def instruction_jal(self, ins: 'LoadedInstruction'):
        reg = 'ra'  # default register is ra
        if len(ins.args) == 1:
            addr = ins.get_imm(0)
        else:
            ASSERT_LEN(ins.args, 2)
            reg = ins.get_reg(0)
            addr = ins.get_imm(1)
        self.regs.set(reg, self.pc)
        self.pc = addr

    def instruction_jalr(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 2)
        reg = ins.get_reg(0)
        addr = ins.get_imm(1)
        self.regs.set(reg, self.pc)
        self.pc = addr

    def instruction_ret(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 0)
        self.pc = self.regs.get('ra')

    def instruction_ecall(self, ins: 'LoadedInstruction'):
        self.instruction_scall(ins)

    def instruction_ebreak(self, ins: 'LoadedInstruction'):
        self.instruction_sbreak(ins)

    def instruction_scall(self, ins: 'LoadedInstruction'):
        ASSERT_LEN(ins.args, 0)
        syscall = Syscall(self.regs.get('a7'), self.regs, self.cpu)
        self.cpu.syscall_int.handle_syscall(syscall)

    def instruction_sbreak(self, ins: 'LoadedInstruction'):
        launch_debug_session(self.cpu, self.mmu, self.regs, "Debug instruction encountered at 0x{:08X}".format(self.pc))

    def instruction_nop(self, ins: 'LoadedInstruction'):
        pass

    def get_reg(self, ins: 'LoadedInstruction', ind: int):
        return self.regs.get(ins.get_reg(ind))