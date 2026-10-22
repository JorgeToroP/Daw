interface FormaGeometrica {
  getArea: () => number;
}

class Rectangulo implements FormaGeometrica {

  public constructor(protected readonly width: number, protected readonly height: number) {}

  public getArea(): number {
    return this.width * this.height;
  }

  public toString(): string {
    return `Rectangulo[width=${this.width}, height=${this.height}]`;
  }
}

class Cuadrado extends Rectangulo {
  public constructor(width: number) {
    super(width, width); //Llamada al constructor del padre
  }

  // Remplazamos el toString de Rectangulo
  public override toString(): string {
    return `Cuadrado[width=${this.width}]`;
  }
}