import { Component } from '@angular/core';
import { CourseService } from '../../../services/course.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ICourse } from '../../../models/ICourse';

@Component({
  selector: 'app-course-register',
  templateUrl: './course-register.component.html',
  styleUrl: './course-register.component.css'
})
export class CourseRegisterComponent {
  isEditing!: boolean;

  course?: ICourse | null;
  formGroupCourse: FormGroup

  constructor(private formBuilder: FormBuilder, private courseService: CourseService) {
    this.formGroupCourse = formBuilder.group({
      cod_curso: [''],
      nome: [''],
      eixo_tecnologico: [''],
    })
  }

  ngOnInit(): void {
      this.isEditing = false;

      this.course = this.courseService.getSharedCourse();

      if (Object.keys(this.course).length > 0) {
        this.formGroupCourse.patchValue({
          cod_curso: this.course.cod_curso,
          nome: this.course.nome,
          eixo_tecnologico: this.course.eixo_tecnologico,
        });
        this.isEditing = true;
      } else {
        this.formGroupCourse.reset();
        this.isEditing = false;
      }

      this.courseService.setSharedCourse({} as ICourse);
  }

  saveCourse(): void {
    if (this.isEditing) {
      this.courseService.updateCourse(this.formGroupCourse.value).subscribe({
        next: (data) => {
          this.formGroupCourse.reset();
          this.isEditing = false;
        }
      });
    } else {
      this.courseService.saveCourse(this.formGroupCourse.value).subscribe({
        next: (data) => {
          this.formGroupCourse.reset();
        }
      })
    }
  }
}
