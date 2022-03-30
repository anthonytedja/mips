window.onload = function() {  
    let instruction = localStorage.getItem('mips-instruction');
    if (instruction) {
        $('#instruction').val(instruction);
        decode(instruction.replace(/\s/g, ''));
}
};  

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
	'use strict';

	// Fetch all the forms we want to apply custom Bootstrap validation styles to
	var forms = document.querySelectorAll('.needs-validation');

	// Loop over them and prevent submission
	Array.prototype.slice.call(forms).forEach(function(form) {
		form.addEventListener(
			'submit',
			function(event) {
				if (!form.checkValidity()) {
					event.preventDefault();
					event.stopPropagation();
				} else {
					var instruction = $('#instruction').val().replace(/\s/g, '');
					decode(instruction);
				}

				form.classList.add('was-validated');
			},
			false
		);
	});
})();

const dic = {
	'100000r': 'add',
	'100001r': 'addu',
	'001000i': 'addi',
	'001001i': 'addiu',
	'011010r': 'div',
	'011011r': 'divu',
	'011000r': 'mult',
	'011001r': 'multu',
	'100010r': 'sub',
	'100011r': 'subu',
	'100100r': 'and',
	'001100i': 'andi',
	'100111r': 'nor',
	'100101r': 'or',
	'001101i': 'ori',
	'100110r': 'xor',
	'001110i': 'xori',
	'000000r': 'sll',
	'000100r': 'sllv',
	'000011r': 'sra',
	'000111r': 'srav',
	'000010r': 'srl',
	'000110r': 'srlv',
	'000100i': 'beq',
	'000111i': 'bgtz',
	'000110i': 'blez',
	'000101i': 'bne',
	'000010j': 'j',
	'000011j': 'jal',
	'001001r': 'jalr',
	'001000r': 'jr',
	'100000i': 'lb',
	'100100i': 'lbu',
	'100001i': 'lh',
	'100101i': 'lhu',
	'100011i': 'lw',
	'101000i': 'sb',
	'101001i': 'sh',
	'101011i': 'sw',
	'010000r': 'mfhi',
	'010010r': 'mflo',
	'101010r': 'slt',
	'101001r': 'sltu',
	'001010i': 'slti',
	'001001i': 'sltiu'
};

const register = [
	'$zero',
	'$at',
	'$v0',
	'$v1',
	'$a0',
	'$a1',
	'$a2',
	'$a3',
	'$t0',
	'$t1',
	'$t2',
	'$t3',
	'$t4',
	'$t5',
	'$t6',
	'$t7',
	'$s0',
	'$s1',
	'$s2',
	'$s3',
	'$s4',
	'$s5',
	'$s6',
	'$s7',
	'$t8',
	'$t9',
	'$k0',
	'$k1',
	'$gp',
	'$sp',
	'$fp',
	'$ra'
];

function decode(instruction) {
    localStorage.setItem('mips-instruction', $('#instruction').val());
	var output = $('#output');

	let rs = instruction.slice(6, 11);
	let rt = instruction.slice(11, 16);
	let rsn = parseInt(rs, 2);
	let rtn = parseInt(rt, 2);

	let opcode = instruction.slice(0, 6);
	let funct = instruction.slice(26);
	let rkey = funct + 'r';
	let ikey = opcode + 'i';
	let jkey = opcode + 'j';

	if (!opcode.includes('1') && rkey in dic) {
		let destination = instruction.slice(16, 21);
		let destn = parseInt(destination, 2);
		let shamt = instruction.slice(21, 26);

		let text = 'R-TYPE \nOPCODE: ' + opcode;
		text += '\nRS: ' + rs + ' ( register ' + rsn + ' ' + register[rsn] + ' )';
		text += '\nRT: ' + rt + ' ( register ' + rtn + ' ' + register[rtn] + ' )';
		text += '\nDEST: ' + destination + ' ( register ' + destn + ' ' + register[destn] + ' )';
		text += '\nSHAMT: ' + shamt + ' ( ' + parseInt(shamt, 2) + ' bits )';
		text += '\nFUNCT: ' + funct + ' ( ' + dic[rkey] + ' )';

		output.text(text);
	} else if (ikey in dic) {
		let immediate = instruction.slice(16);
		let shift = parseInt(immediate.slice(2) + '00', 2);

		if ((shift & (1 << (16 - 1))) != 0) {
			shift = shift - (1 << 16);
		}

		let text = 'I-TYPE \nOPCODE: ' + opcode + ' ( ' + dic[ikey] + ' )';
		text += '\nRS: ' + rs + ' ( register ' + rsn + ' ' + register[rsn] + ' )';
		text += '\nRT: ' + rt + ' ( register ' + rtn + ' ' + register[rtn] + ' )';
		text += '\nIMMED: ' + immediate + ' ( ' + parseInt(immediate, 2) + ' ) ';
		text += '( With Shift ' + shift.toString() + ' )';

		output.text(text);
	} else if (jkey in dic) {
		let address = instruction.slice(6);
		let adrn = parseInt(address, 2);
		let shift = adrn << 2;

		let text = 'J-TYPE \nOPCODE: ' + opcode + ' ( ' + dic[jkey] + ' )';
		text += '\nADR: ' + address + ' ( ' + adrn + ' )';
		text += '( With Shift ' + shift.toString() + ' )';

		output.text(text);
	} else {
		let text = 'MIPS instruction not found';
		output.text(text);
	}

	output.html(output.html().replace(/\n/g, '<br/>'));
}
