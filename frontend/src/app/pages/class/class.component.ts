import { Component } from '@angular/core';
import { IClass } from '../../models/IClass';
import { ClassService } from '../../services/class.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-class',
  templateUrl: './class.component.html',
  styleUrl: './class.component.css'
})
export class ClassComponent {
  classes: IClass[] = [];

  constructor(private classService: ClassService, private _router: Router) {}

  ngOnInit(): void {
    this.loadClasses();
  }

  loadClasses(): void {
    this.classService.getClasses().subscribe({
      next: (data) => {
        this.classes = data;
      }
    })
  }

  updateClass(classObj: IClass): void {
    this.classService.setSharedClass(classObj);
    this._router.navigate(['/class/register', {data: {isEditing: true}}]);
  }

  deleteClass(classObj: IClass): void {
    this.classService.deleteClass(classObj).subscribe({
      next: (data) => {
        this.loadClasses();
      }
    })
  }
}
