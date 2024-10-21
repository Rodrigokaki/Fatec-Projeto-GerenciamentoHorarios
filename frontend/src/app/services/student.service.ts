import { Injectable } from '@angular/core';
import { IStudent } from '../models/IStudent';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StudentService {

  url = "http://127.0.0.1:5000/students";

  private sharedStudent: IStudent = {} as IStudent;

  constructor(private http: HttpClient) { }

  getSharedStudent(): IStudent {
    return this.sharedStudent;
  }

  setSharedStudent(student: IStudent): void {
    this.sharedStudent = student;
  }

  getStudents(): Observable<IStudent[]> {
    return this.http.get<IStudent[]>(this.url);
  }

  getStudentId(studentId: number): Observable<IStudent> {
    return this.http.get<IStudent>(`${this.url}/${studentId}`);
  }

  saveStudent(student: IStudent): Observable<IStudent> {
    return this.http.post<IStudent>(this.url, student);
  }

  deleteStudent(student: IStudent): Observable<void> {
    return this.http.delete<void>(`${this.url}/${student.cod_aluno}`);
  }

  updateStudent(student: IStudent): Observable<IStudent> {
    return this.http.put<IStudent>(`${this.url}/${student.cod_aluno}`, student);
  }
}
