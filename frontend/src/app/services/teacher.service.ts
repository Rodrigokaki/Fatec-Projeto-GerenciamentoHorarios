import { Injectable } from '@angular/core';
import { ITeacher } from '../models/ITeacher';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TeacherService {

  url = "http://127.0.0.1:5000/teachers";

  private sharedTeacher: ITeacher = {} as ITeacher;

  constructor(private http: HttpClient) { }

  getSharedTeacher(): ITeacher {
    return this.sharedTeacher;
  }

  setSharedTeacher(teacher: ITeacher): void {
    this.sharedTeacher = teacher;
  }

  getTeachers(): Observable<ITeacher[]> {
    return this.http.get<ITeacher[]>(this.url);
  }

  getTeacherId(teacherId: number): Observable<ITeacher> {
    return this.http.get<ITeacher>(`${this.url}/${teacherId}`);
  }

  saveTeacher(teacher: ITeacher): Observable<ITeacher> {
    return this.http.post<ITeacher>(this.url, teacher);
  }

  deleteTeacher(teacher: ITeacher): Observable<void> {
    return this.http.delete<void>(`${this.url}/${teacher.cod_prof}`);
  }

  updateTeacher(teacher: ITeacher): Observable<ITeacher> {
    return this.http.put<ITeacher>(`${this.url}/${teacher.cod_prof}`, teacher);
  }
}
