import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SaludoAmorcito } from './saludo-amorcito';

describe('SaludoAmorcito', () => {
  let component: SaludoAmorcito;
  let fixture: ComponentFixture<SaludoAmorcito>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SaludoAmorcito],
    }).compileComponents();

    fixture = TestBed.createComponent(SaludoAmorcito);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
