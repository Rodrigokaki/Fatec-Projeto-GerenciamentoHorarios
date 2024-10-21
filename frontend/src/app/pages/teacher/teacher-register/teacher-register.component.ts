import { Component } from '@angular/core';
import { ITeacher } from '../../../models/ITeacher';
import { FormBuilder, FormGroup } from '@angular/forms';
import { TeacherService } from '../../../services/teacher.service';

@Component({
  selector: 'app-teacher-register',
  templateUrl: './teacher-register.component.html',
  styleUrl: './teacher-register.component.css'
})
export class TeacherRegisterComponent {
  isEditing!: boolean;

  teacher?: ITeacher | null;
  formGroupTeacher: FormGroup

  constructor(private formBuilder: FormBuilder, private teacherService: TeacherService) {
    this.formGroupTeacher = formBuilder.group({
      cod_prof: [''],
      nome: [''],
      cpf: [''],
      email_institucional: [''],
      data_admissao: [''],
    })
  }

  ngOnInit(): void {
      this.isEditing = false;

      this.teacher = this.teacherService.getSharedTeacher();

      if (Object.keys(this.teacher).length > 0) {
        this.formGroupTeacher.patchValue({
          cod_prof: this.teacher.cod_prof,
          nome: this.teacher.nome,
          cpf: this.teacher.cpf,
          email_institucional: this.teacher.email_institucional,
          data_admissao: this.teacher.data_admissao,
        });
        this.isEditing = true;
      } else {
        this.formGroupTeacher.reset();
        this.isEditing = false;
      }

      this.teacherService.setSharedTeacher({} as ITeacher);
  }

  saveTeacher(): void {
    if (this.isEditing) {
      this.teacherService.updateTeacher(this.formGroupTeacher.value).subscribe({
        next: (data) => {
          this.formGroupTeacher.reset();
          this.isEditing = false;
        }
      });
    } else {
      this.teacherService.saveTeacher(this.formGroupTeacher.value).subscribe({
        next: (data) => {
          this.formGroupTeacher.reset();
        }
      })
    }
  }
}
