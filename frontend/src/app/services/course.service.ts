import { Injectable } from '@angular/core';
import { ICourse } from '../models/ICourse';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  url = "http://127.0.0.1:5000/courses";

  private sharedCourse: ICourse = {} as ICourse;

  constructor(private http: HttpClient) { }

  getSharedCourse(): ICourse {
    return this.sharedCourse;
  }

  setSharedCourse(course: ICourse): void {
    this.sharedCourse = course;
  }

  getCourses(): Observable<ICourse[]> {
    return this.http.get<ICourse[]>(this.url);
  }

  getCourseId(courseId: number): Observable<ICourse> {
    return this.http.get<ICourse>(`${this.url}/${courseId}`);
  }

  saveCourse(course: ICourse): Observable<ICourse> {
    return this.http.post<ICourse>(this.url, course);
  }

  deleteCourse(course: ICourse): Observable<void> {
    return this.http.delete<void>(`${this.url}/${course.cod_curso}`);
  }

  updateCourse(course: ICourse): Observable<ICourse> {
    return this.http.put<ICourse>(`${this.url}/${course.cod_curso}`, course);
  }
}
