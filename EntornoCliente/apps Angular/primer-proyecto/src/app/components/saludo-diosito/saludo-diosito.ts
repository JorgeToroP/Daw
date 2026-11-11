import { Component,OnInit } from '@angular/core';



@Component({
  imports: [],
  selector: 'app-saludo-diosito',
  styleUrl: './saludo-diosito.css',
  templateUrl: './saludo-diosito.html',
})


export class SaludoDiosito implements OnInit {
nombre = 'YHWHW';
constructor() {
console.log('1. constructor');
}
ngOnInit(): void {
console.log('2. ngOnInit');
}
}