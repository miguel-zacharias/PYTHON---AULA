// Exercício 11 — Operadores em Múltiplas Linguagens (JavaScript)
// Exercício 3: Operador Módulo (%)
const prompt = require('prompt-sync')();
const num = parseInt(prompt('Digite um número: '));

const resto2 = num % 2;
const resto3 = num % 3;
const resto5 = num % 5;
const resto10 = num % 10;
const parOuImpar = resto2 === 0 ? 'par' : 'ímpar';

console.log(`Resto por 2: ${resto2} (Número ${parOuImpar})`);
console.log(`Resto por 3: ${resto3}`);
console.log(`Resto por 5: ${resto5}`);
console.log(`Resto por 10: ${resto10}`);

// Exercício 4: Operadores Relacionais
const num1 = parseInt(prompt('Digite o primeiro número: '));
const num2 = parseInt(prompt('Digite o segundo número: '));

console.log(`${num1} > ${num2} : ${num1 > num2}`);
console.log(`${num1} < ${num2} : ${num1 < num2}`);
console.log(`${num1} == ${num2} : ${num1 == num2}`);
console.log(`${num1} != ${num2} : ${num1 != num2}`);
console.log(`${num1} >= ${num2} : ${num1 >= num2}`);
console.log(`${num1} <= ${num2} : ${num1 <= num2}`);
