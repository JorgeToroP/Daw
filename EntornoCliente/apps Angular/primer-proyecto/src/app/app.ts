import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SaludoDiosito } from './components/saludo-diosito/saludo-diosito';
import { SaludoAmorcito } from './components/saludo-amorcito/saludo-amorcito';
import { Calculadora } from './components/calculadora/calculadora';
@Component({
  imports: [Calculadora, SaludoDiosito, SaludoAmorcito, RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('primer-proyecto');
}
