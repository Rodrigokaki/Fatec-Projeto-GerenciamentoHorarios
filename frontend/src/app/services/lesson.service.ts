import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { ILesson } from '../models/ILesson';

@Injectable({
  providedIn: 'root'
})
export class LessonService {

  url = "http://127.0.0.1:5000/lessons";

  private sharedLesson: ILesson = {} as ILesson;

  constructor(private http: HttpClient) { }

  getSharedLesson(): ILesson {
    return this.sharedLesson;
  }

  setSharedLesson(lesson: ILesson): void {
    this.sharedLesson = lesson;
  }

  getLessons(): Observable<ILesson[]> {
    return this.http.get<ILesson[]>(this.url);
  }

  getLessonId(lessonId: number): Observable<ILesson> {
    return this.http.get<ILesson>(`${this.url}/${lessonId}`);
  }

  saveLesson(lesson: ILesson): Observable<ILesson> {
    return this.http.post<ILesson>(this.url, lesson);
  }

  deleteLesson(lesson: ILesson): Observable<void> {
    return this.http.delete<void>(`${this.url}/${lesson.cod_aula}`);
  }

  updateLesson(lesson: ILesson): Observable<ILesson> {
    return this.http.put<ILesson>(`${this.url}/${lesson.cod_aula}`, lesson);
  }

}
