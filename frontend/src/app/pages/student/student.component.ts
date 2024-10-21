import { Component } from '@angular/core';
import { IStudent } from '../../models/IStudent';
import { StudentService } from '../../services/student.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-student',
  templateUrl: './student.component.html',
  styleUrl: './student.component.css'
})
export class StudentComponent {
  students: IStudent[] = [];

  constructor(private studentService: StudentService, private _router: Router) {}

  ngOnInit(): void {
    this.loadStudents();
  }

  loadStudents(): void {
    this.studentService.getStudents().subscribe({
      next: (data) => {
        this.students = data;
      }
    })
  }

  updateStudent(student: IStudent): void {
    this.studentService.setSharedStudent(student);
    this._router.navigate(['/student/register', {data: {isEditing: true}}]);
  }

  deleteStudent(student: IStudent): void {
    this.studentService.deleteStudent(student).subscribe({
      next: (data) => {
        this.loadStudents();
      }
    })
  }
}
