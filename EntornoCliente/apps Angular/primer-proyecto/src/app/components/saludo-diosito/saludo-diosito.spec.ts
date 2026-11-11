import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SaludoDiosito } from './saludo-diosito';

describe('SaludoDiosito', () => {
  let component: SaludoDiosito;
  let fixture: ComponentFixture<SaludoDiosito>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SaludoDiosito],
    }).compileComponents();

    fixture = TestBed.createComponent(SaludoDiosito);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
