//Dichiarazione di Variabile
var x = 1;
console.log(x);
console.log(x+1);

//Stringhe
console.log("Alessio Manfredini".toUpperCase());

//Infinity
console.log(8/0);
console.log(-8/0);

//Operatori
console.log(true && false); //AND
console.log(false || true); //OR
console.log(!1); //NOT

//Array
var arr = [
    "lunedì",
    "martedì",
    "mercoledì",
    "giovedì",
    "venerdì",
    "sabato",
    "domenica"
];
console.log(arr);
console.log(arr[2]);

//Istruzioni Condizionali
if (arr[0] == "lunedì")
    console.log("è lunedì");
else
    console.log("non è lunedì");

switch(arr[0]){
    case "martedì":
        console.log("non è lunedì");
        break;
    case "lunedì":
        console.log("è lunedì");
        break;
    default:
        //
        break;
}

//Cicli
var x = 10;
while (x > 0){
    x -= 1;
    console.log(x);
}
console.log();
x = 10;
do{
    x -= 1;
    console.log(x);
} while(x > 0);
console.log();
for (i = 0; i<10; i++)
    console.log(i);
console.log();

for (indice in arr)
    console.log(indice);
for (giorno of arr)
    console.log(giorno);

//Funzioni
function nome(argomenti) {
    // istruzioni
}
    
//Oggetti
var oggettoVuoto = {};
console.log();
var persona = { "nome": "Mario", "cognome": "Rossi"};
console.log(persona);
var persona = {
	nome: "Mario",
	cognome: "Rossi",
	indirizzo: {
		via: "Via Garibaldi",
		numero: 15,
		CAP: "00100",
		citta: "Roma"
	},
    nomeCognome: function () {return this.nome + " " + this.cognome; }
};
console.log(persona);
console.log(persona.nome);
console.log(persona.nomeCognome());

//Arrow Function
/*
Si tratta di funzioni anonime con una sintassi molto concisa ed alcune specifiche caratteristiche
*/
var somma = (x, y) => { return x + y; }
console.log(somma(1,2));