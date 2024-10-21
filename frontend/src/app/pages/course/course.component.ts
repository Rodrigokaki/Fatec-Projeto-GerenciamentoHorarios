import { Component } from '@angular/core';
import { ICourse } from '../../models/ICourse';
import { CourseService } from '../../services/course.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrl: './course.component.css'
})
export class CourseComponent {
  courses: ICourse[] = [];

  constructor(private courseService: CourseService, private _router: Router) {}

  ngOnInit(): void {
    this.loadCourses();
  }

  loadCourses(): void {
    this.courseService.getCourses().subscribe({
      next: (data) => {
        this.courses = data;
      }
    })
  }

  updateCourse(course: ICourse): void {
    this.courseService.setSharedCourse(course);
    this._router.navigate(['/course/register', {data: {isEditing: true}}]);
  }

  deleteCourse(course: ICourse): void {
    this.courseService.deleteCourse(course).subscribe({
      next: (data) => {
        this.loadCourses();
      }
    })
  }
}
