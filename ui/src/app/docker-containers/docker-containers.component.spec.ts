import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DockerContainersComponent } from './docker-containers.component';

describe('DockerContainersComponent', () => {
  let component: DockerContainersComponent;
  let fixture: ComponentFixture<DockerContainersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DockerContainersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DockerContainersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
