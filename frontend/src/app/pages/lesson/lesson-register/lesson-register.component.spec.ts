import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LessonRegisterComponent } from './lesson-register.component';

describe('LessonRegisterComponent', () => {
  let component: LessonRegisterComponent;
  let fixture: ComponentFixture<LessonRegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LessonRegisterComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LessonRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
