import { Injectable } from '@angular/core';
import { ISubject } from '../models/ISubject';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SubjectService {

  url = "http://127.0.0.1:5000/subjects";

  private sharedSubject: ISubject = {} as ISubject;

  constructor(private http: HttpClient) { }

  getSharedSubject(): ISubject {
    return this.sharedSubject;
  }

  setSharedSubject(subject: ISubject): void {
    this.sharedSubject = subject;
  }

  getSubjects(): Observable<ISubject[]> {
    return this.http.get<ISubject[]>(this.url);
  }

  getSubjectId(subjectId: number): Observable<ISubject> {
    return this.http.get<ISubject>(`${this.url}/${subjectId}`);
  }

  saveSubject(subject: ISubject): Observable<ISubject> {
    return this.http.post<ISubject>(this.url, subject);
  }

  deleteSubject(subject: ISubject): Observable<void> {
    return this.http.delete<void>(`${this.url}/${subject.cod_disciplina}`);
  }

  updateSubject(subject: ISubject): Observable<ISubject> {
    return this.http.put<ISubject>(`${this.url}/${subject.cod_disciplina}`, subject);
  }
}
