# from queue import Queue

# class DataProcess(QObject):
#     def __init__(self, arduino, ui):
#         super().__init__()
#         self.arduino_thread = arduino
#         self.ui = ui

#         self.data_queue = Queue()
#         self.gauge_data_queue = Queue()

#         self.data_processor_thread = DataProcessorThread(self.data_queue)
#         self.gauge_updater_thread = GaugeUpdaterThread(self.ui, self.gauge_data_queue)

#         self.arduino_thread.data_received.connect(self.enqueue_data)
#         self.data_processor_thread.processed_data.connect(self.enqueue_processed_data)

#         self.data_processor_thread.start()
#         self.gauge_updater_thread.start()

#     def enqueue_data(self, data):
#         self.data_queue.put(data)

#     def enqueue_processed_data(self, processed_data):
#         self.gauge_data_queue.put(processed_data)

#     def closeEvent(self, event):
#         self.data_processor_thread.stop()
#         self.data_processor_thread.wait()
#         self.gauge_updater_thread.stop()
#         self.gauge_updater_thread.wait()
#         self.arduino_thread.stop()
#         self.arduino_thread.wait()
#         self.arduino.close()
#         event.accept()
