import { Component, Input, OnInit } from '@angular/core';
import { ILesson } from '../../../models/ILesson';
import { FormBuilder, FormGroup } from '@angular/forms';
import { LessonService } from '../../../services/lesson.service';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { ISubject } from '../../../models/ISubject';
import { SubjectService } from '../../../services/subject.service';
import { IClass } from '../../../models/IClass';
import { ClassService } from '../../../services/class.service';
import { IClassName } from '../../../models/IClassName';

@Component({
  selector: 'app-lesson-register',
  templateUrl: './lesson-register.component.html',
  styleUrl: './lesson-register.component.css'
})
export class LessonRegisterComponent implements OnInit {
  @Input() isEditing!: boolean;

  lesson?: ILesson | null;
  formGroupLesson: FormGroup
  subjects: ISubject[] = [];
  classes: IClass[] = [];
  classesWithName: IClassName[] = [];

  constructor(private formBuilder: FormBuilder, private lessonService: LessonService, private subjectService: SubjectService, 
    private classService: ClassService) {
    this.formGroupLesson = formBuilder.group({
      cod_aula: [''],
      horario: [''],
      cod_disciplina: [''],
      cod_turma: [''],
      dia_semana: ['']
    })
  }

  ngOnInit(): void {
      this.isEditing = false;

      this.subjectService.getSubjects().subscribe(data => {
        this.subjects = data;
      })

      this.classService.getClassesWithName().subscribe(data => {
        this.classesWithName = data;
      })

      this.lesson = this.lessonService.getSharedLesson();

      if (Object.keys(this.lesson).length > 0) {
        this.formGroupLesson.patchValue({
          cod_aula: this.lesson.cod_aula,
          cod_disciplina: this.lesson.cod_disciplina,
          cod_turma: this.lesson.cod_turma,
          horario: this.lesson.horario,
          dia_semana: this.lesson.dia_semana
        });
        this.isEditing = true;
      } else {
        this.formGroupLesson.reset();
        this.isEditing = false;
      }

      this.lessonService.setSharedLesson({} as ILesson);
  }

  saveLesson(): void {
    if (this.isEditing) {
      this.lessonService.updateLesson(this.formGroupLesson.value).subscribe({
        next: (data) => {
          this.formGroupLesson.reset();
          this.isEditing = false;
        }
      });
    } else {
      this.lessonService.saveLesson(this.formGroupLesson.value).subscribe({
        next: (data) => {
          this.formGroupLesson.reset();
        }
      })
    }
  }
}
