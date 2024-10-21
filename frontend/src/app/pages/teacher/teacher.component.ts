import { Component } from '@angular/core';
import { ITeacher } from '../../models/ITeacher';
import { TeacherService } from '../../services/teacher.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-teacher',
  templateUrl: './teacher.component.html',
  styleUrl: './teacher.component.css'
})
export class TeacherComponent {
  teachers: ITeacher[] = [];

  constructor(private teacherService: TeacherService, private _router: Router) {}

  ngOnInit(): void {
    this.loadTeachers();
  }

  loadTeachers(): void {
    this.teacherService.getTeachers().subscribe({
      next: (data) => {
        this.teachers = data;
      }
    })
  }

  updateTeacher(teacher: ITeacher): void {
    this.teacherService.setSharedTeacher(teacher);
    this._router.navigate(['/teacher/register', {data: {isEditing: true}}]);
  }

  deleteTeacher(teacher: ITeacher): void {
    this.teacherService.deleteTeacher(teacher).subscribe({
      next: (data) => {
        this.loadTeachers();
      }
    })
  }
}
