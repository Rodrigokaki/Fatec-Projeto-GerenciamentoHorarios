import { Component } from '@angular/core';
import { ISubject } from '../../../models/ISubject';
import { SubjectService } from '../../../services/subject.service';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-subject-register',
  templateUrl: './subject-register.component.html',
  styleUrl: './subject-register.component.css'
})
export class SubjectRegisterComponent {
  isEditing!: boolean;

  subject?: ISubject | null;
  formGroupSubject: FormGroup

  constructor(private formBuilder: FormBuilder, private subjectService: SubjectService) {
    this.formGroupSubject = formBuilder.group({
      cod_disciplina: [''],
      nome: [''],
      cod_prof: [''],
      cod_curso: [''],
    })
  }

  ngOnInit(): void {
      this.isEditing = false;

      this.subject = this.subjectService.getSharedSubject();

      if (Object.keys(this.subject).length > 0) {
        this.formGroupSubject.patchValue({
          cod_disciplina: this.subject.cod_prof,
          nome: this.subject.nome,
          cod_prof: this.subject.cod_prof,
          cod_curso: this.subject.cod_curso,
        });
        this.isEditing = true;
      } else {
        this.formGroupSubject.reset();
        this.isEditing = false;
      }

      this.subjectService.setSharedSubject({} as ISubject);
  }

  saveSubject(): void {
    if (this.isEditing) {
      this.subjectService.updateSubject(this.formGroupSubject.value).subscribe({
        next: (data) => {
          this.formGroupSubject.reset();
          this.isEditing = false;
        }
      });
    } else {
      this.subjectService.saveSubject(this.formGroupSubject.value).subscribe({
        next: (data) => {
          this.formGroupSubject.reset();
        }
      })
    }
  }
}
