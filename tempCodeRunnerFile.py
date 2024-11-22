       
        
        self.ui.stackedWidget.setCurrentIndex(0)
        self.design_gauges()
        # print('i am here')
        self.worker_arduino = WorkerArduino(self.ui,'COM14')
        # self.worker_arduino = WorkerArduino(self.ui, "/dev/ttyACM0")
        # self.worker_arduino.data_received.connect(self.process_serial_data)
        self.worker_arduino.start()
        # self.update_worker = UpdateWorker(self.ui)
        # self.update_worker.start()
        self.check_table()
        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.update_time
        )  # Connect timeout to the update function
        self.timer.start(1000)  # 1000 ms = 1 second
        # Call update_time once at startup to set the initial time
        self.update_time()
