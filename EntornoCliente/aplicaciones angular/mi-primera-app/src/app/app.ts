import { Component, signal } from '@angular/core';
import { Saludo } from './components/saludo/saludo';

@Component({
  imports: [Saludo],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('mi-primera-app');
}
