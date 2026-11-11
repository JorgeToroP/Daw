import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [FormsModule],
  selector: 'app-calculadora',
  styleUrl: './calculadora.css',
  templateUrl: './calculadora.html',
})
export class Calculadora {
  numeroA = 0;
  numeroB = 0;
  resultado = 0;

  sumar() {
    this.resultado = this.numeroA + this.numeroB;
  }

  restar() {
    this.resultado = this.numeroA - this.numeroB;
  }

  multiplicar() {
    this.resultado = this.numeroA * this.numeroB;
  }

  dividir() {
    if (this.numeroB !== 0) {
      this.resultado = this.numeroA / this.numeroB;
    } else {
      alert('No se puede dividir entre cero');
    }
  }
}
