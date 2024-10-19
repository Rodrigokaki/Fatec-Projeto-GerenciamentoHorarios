import { Component, OnInit } from '@angular/core';
import { LessonService } from '../../services/lesson.service';
import { ILesson } from '../../models/ILesson';
import { Router } from '@angular/router';

@Component({
  selector: 'app-lesson',
  templateUrl: './lesson.component.html',
  styleUrl: './lesson.component.css'
})
export class LessonComponent implements OnInit {
  lessons: ILesson[] = [];

  constructor(private lessonService: LessonService, private _router: Router) {}

  ngOnInit(): void {
    this.loadLessons();
  }

  loadLessons(): void {
    this.lessonService.getLessons().subscribe({
      next: (data) => {
        this.lessons = data;
      }
    })
  }

  updateLesson(lesson: ILesson): void {
    this.lessonService.setSharedLesson(lesson);
    this._router.navigate(['/lesson/register', {data: {isEditing: true}}]);
  }

  deleteLesson(lesson: ILesson): void {
    this.lessonService.deleteLesson(lesson).subscribe({
      next: (data) => {
        this.loadLessons();
      }
    })
  }
}
