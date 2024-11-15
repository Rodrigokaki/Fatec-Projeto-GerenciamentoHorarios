import { Component } from '@angular/core';
import { IClass } from '../../../models/IClass';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ClassService } from '../../../services/class.service';
import { IClassName } from '../../../models/IClassName';
import { ICourse } from '../../../models/ICourse';
import { CourseService } from '../../../services/course.service';

@Component({
  selector: 'app-class-register',
  templateUrl: './class-register.component.html',
  styleUrl: './class-register.component.css'
})
export class ClassRegisterComponent {
  isEditing!: boolean;

  classObj?: IClass | null;
  formGroupClass: FormGroup
  courses: ICourse[] = [];

  constructor(private formBuilder: FormBuilder, private classService: ClassService, private courseService: CourseService) {
    this.formGroupClass = formBuilder.group({
      cod_turma: [''],
      semestre: [''],
      periodo: [''],
      ano: [''],
      cod_curso: [''],
    })
  }

  ngOnInit(): void {
      this.isEditing = false;

      this.classObj = this.classService.getSharedClass();

      this.courseService.getCourses().subscribe(data => {
        this.courses = data;
      })

      if (Object.keys(this.classObj).length > 0) {
        this.formGroupClass.patchValue({
          cod_turma: this.classObj.cod_turma,
          semestre: this.classObj.semestre,
          periodo: this.classObj.periodo,
          ano: this.classObj.ano,
          cod_curso: this.classObj.cod_curso,
        });
        this.isEditing = true;
      } else {
        this.formGroupClass.reset();
        this.isEditing = false;
      }

      this.classService.setSharedClass({} as IClass);
  }

  saveClass(): void {
    if (this.isEditing) {
      this.classService.updateClass(this.formGroupClass.value).subscribe({
        next: (data) => {
          this.formGroupClass.reset();
          this.isEditing = false;
        }
      });
    } else {
      this.classService.saveClass(this.formGroupClass.value).subscribe({
        next: (data) => {
          this.formGroupClass.reset();
        }
      })
    }
  }
}
