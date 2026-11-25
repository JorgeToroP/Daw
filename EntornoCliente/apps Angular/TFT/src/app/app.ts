import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Inicio } from './components/inicio/inicio';
import { CommonModule } from '@angular/common';
import { Usuarios } from './components/usuarios/usuarios';

@Component({
  imports: [RouterOutlet, Inicio, CommonModule, Usuarios],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('TFT');
}
