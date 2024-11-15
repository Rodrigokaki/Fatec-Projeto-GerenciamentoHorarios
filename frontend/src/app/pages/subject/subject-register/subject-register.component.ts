import { Component } from '@angular/core';
import { ISubject } from '../../../models/ISubject';
import { SubjectService } from '../../../services/subject.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ITeacher } from '../../../models/ITeacher';
import { ICourse } from '../../../models/ICourse';
import { TeacherService } from '../../../services/teacher.service';
import { CourseService } from '../../../services/course.service';

@Component({
  selector: 'app-subject-register',
  templateUrl: './subject-register.component.html',
  styleUrl: './subject-register.component.css'
})
export class SubjectRegisterComponent {
  isEditing!: boolean;

  subject?: ISubject | null;
  formGroupSubject: FormGroup
  teachers: ITeacher[] = [];
  courses: ICourse[] = [];

  constructor(private formBuilder: FormBuilder, private subjectService: SubjectService, private teacherService: TeacherService,
    private courseService: CourseService
  ) {
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

      this.teacherService.getTeachers().subscribe(data => {
        this.teachers = data;
      })

      this.courseService.getCourses().subscribe(data => {
        this.courses = data;
      })

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
