# Project Description: Group 19 Canteen Tracker

The **Group 19 Canteen Tracker** is a Python-based data analysis application developed using Streamlit. Its main purpose is to help users manage, analyze, and visualize canteen sales data imported from an Excel (.xlsx) file.

The application allows users to upload an Excel workbook containing canteen order information, including details such as campus, category, item, price, and quantity. Once the file is uploaded, the system validates the data, checks for missing or invalid values, and calculates the total amount for each order by multiplying the price by the quantity.

Users can filter the displayed orders by campus and category, making it easier to analyze specific sections of the canteen's sales. The application also provides a summary of important sales information, including total sales, the number of orders, the average order value, and the best-selling item.

To make the information easier to understand, the Canteen Tracker presents sales data through tables and visual charts. These include a histogram showing the distribution of order values in J$500 ranges, a bar chart displaying total sales by item, and a line chart showing sales over time.

Additionally, the application includes a CSV download feature that allows users to export their filtered order data for further analysis or record-keeping.

The project is organized into **22 functions**, consisting of 13 service functions responsible for data processing, calculations, filtering, validation, and exporting, and 9 screen functions responsible for displaying the application's interface using Streamlit.

Overall, the Group 19 Canteen Tracker aims to make canteen sales management more efficient by reducing manual calculations, identifying data errors, organizing sales information, and providing useful insights that can support better business decisions.
