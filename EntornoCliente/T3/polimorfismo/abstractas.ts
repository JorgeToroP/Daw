abstract class Poligono {
  public abstract getArea(): number;
  public toString(): string {
    return `Poligono [area=${this.getArea()}]`;
  }
}
class Rectangulo extends Poligono {
  public constructor(protected readonly width: number, protected readonly height: number) {
    super();
  }
  public getArea(): number {
    return this.width * this.height;
  }
}