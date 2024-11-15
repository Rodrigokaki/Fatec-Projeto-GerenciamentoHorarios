import { Component } from '@angular/core';
import { IStudent } from '../../../models/IStudent';
import { StudentService } from '../../../services/student.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { IClassName } from '../../../models/IClassName';
import { ClassService } from '../../../services/class.service';

@Component({
  selector: 'app-student-register',
  templateUrl: './student-register.component.html',
  styleUrl: './student-register.component.css'
})
export class StudentRegisterComponent {
  isEditing!: boolean;

  student?: IStudent | null;
  formGroupStudent: FormGroup;
  classes: IClassName[] = [];

  constructor(private formBuilder: FormBuilder, private studentService: StudentService, private classService: ClassService) {
    this.formGroupStudent = formBuilder.group({
      cod_aluno: [''],
      cod_turma: [''],
      nome: [''],
      data_matricula: [''],
      data_nascimento: ['']
    })
  }

  ngOnInit(): void {
      this.isEditing = false;

      this.student = this.studentService.getSharedStudent();

      this.classService.getClassesWithName().subscribe(data => {
        this.classes = data;
      })

      if (Object.keys(this.student).length > 0) {
        this.formGroupStudent.patchValue({
          cod_aluno: this.student.cod_aluno,
          cod_turma: this.student.cod_turma,
          nome: this.student.nome,
          data_matricula: this.student.data_matricula,
          data_nascimento: this.student.data_nascimento
        });
        this.isEditing = true;
      } else {
        this.formGroupStudent.reset();
        this.isEditing = false;
      }

      this.studentService.setSharedStudent({} as IStudent);
  }

  saveStudent(): void {
    if (this.isEditing) {
      this.studentService.updateStudent(this.formGroupStudent.value).subscribe({
        next: (data) => {
          this.formGroupStudent.reset();
          this.isEditing = false;
        }
      });
    } else {
      this.studentService.saveStudent(this.formGroupStudent.value).subscribe({
        next: (data) => {
          this.formGroupStudent.reset();
        }
      })
    }
  }
}
