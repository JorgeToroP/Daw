// contador.ts
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-contador',
  templateUrl: './contador.html',
  styleUrl: './contador.css'
})
export class Contador implements OnInit {
  cuenta = 0;
  mensaje = '';

  ngOnInit(): void {
    this.mensaje = 'Contador listo';
  }

  sumar() {
    this.cuenta++;
  }

  reiniciar() {
    this.cuenta = 0;
  }
}

