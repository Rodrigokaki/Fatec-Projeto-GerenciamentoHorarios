import { Component } from '@angular/core';
import { ISubject } from '../../models/ISubject';
import { SubjectService } from '../../services/subject.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-subject',
  templateUrl: './subject.component.html',
  styleUrl: './subject.component.css'
})
export class SubjectComponent {
  subjects: ISubject[] = [];

  constructor(private subjectService: SubjectService, private _router: Router) {}

  ngOnInit(): void {
    this.loadSubjects();
  }

  loadSubjects(): void {
    this.subjectService.getSubjects().subscribe({
      next: (data) => {
        this.subjects = data;
      }
    })
  }

  updateSubject(subject: ISubject): void {
    this.subjectService.setSharedSubject(subject);
    this._router.navigate(['/subject/register', {data: {isEditing: true}}]);
  }

  deleteSubject(subject: ISubject): void {
    this.subjectService.deleteSubject(subject).subscribe({
      next: (data) => {
        this.loadSubjects();
      }
    })
  }
}
