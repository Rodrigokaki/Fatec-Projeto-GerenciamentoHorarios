import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ClassComponent } from './pages/class/class.component';
import { LessonComponent } from './pages/lesson/lesson.component';
import { StudentComponent } from './pages/student/student.component';
import { SubjectComponent } from './pages/subject/subject.component';
import { TeacherComponent } from './pages/teacher/teacher.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'class', component: ClassComponent},
  {path: 'lesson', component: LessonComponent},
  {path: 'student', component: StudentComponent},
  {path: 'subject', component: SubjectComponent},
  {path: 'teacher', component: TeacherComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
