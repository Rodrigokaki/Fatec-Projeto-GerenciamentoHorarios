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
        day: "Domingo",
        data: []
      },
      {
        day: "Segunda-feira",
        data: []
      },
      {
        day: "Terça-feira",
        data: []
      },
      {
        day: "Quarta-feira",
        data: []
      },
      {
        day: "Quinta-feira",
        data: []
      },
      {
        day: "Sexta-feira",
        data: []
      },
      {
        day: "Sábado",
        data: []
      }
    ];

    this.homeService.getView().subscribe({
      next: (data) => {
        for (let row of data) {
          switch (row.DiaSemana) {
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
