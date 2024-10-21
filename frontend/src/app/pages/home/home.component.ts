import { Component, OnInit } from '@angular/core';
import { IHome } from '../../models/IHome';
import { HomeViewService } from '../../services/home-view.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  days!: any;

  constructor(private homeService: HomeViewService) {}

  ngOnInit(): void {
      this.loadRows();
  }

  loadRows(): void {
    this.days = [
      {
        day: 1,
        data: []
      },
      {
        day: 2,
        data: []
      },
      {
        day: 3,
        data: []
      },
      {
        day: 4,
        data: []
      },
      {
        day: 5,
        data: []
      },
      {
        day: 6,
        data: []
      },
      {
        day: 7,
        data: []
      }
    ];

    this.homeService.getView().subscribe({
      next: (data) => {
        for (let row of data) {
          switch (row.dia_semana) {
            case "Segunda-feira":
              this.days[1]['data'].push(row);
              break;
            case "Terça-feira":
              this.days[2]['data'].push(row);
              break;
            case "Quarta-feira":
              this.days[3]['data'].push(row);
              break;
            case "Quinta-feira":
              this.days[4]['data'].push(row);
              break;
            case "Sexta-feira":
              this.days[5]['data'].push(row);
              break;
            case "Sábado":
              this.days[6]['data'].push(row);
              break;
            case "Domingo":
              this.days[0]['data'].push(row);
              break
            default:
              break;
          }
        }
      }
    })
  }
}
