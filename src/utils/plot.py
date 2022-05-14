import matplotlib.pyplot as plt
if __name__ == '__main__':
    x = range(1000)
    a_y = [20.85, 19.54, 20.85, 26.4, 18.48, 18.47, 18.66, 18.29, 22.16, 20.86, 20.73, 20.85, 24.51, 17.73, 19.47, 20.3, 21.28, 18.78, 27.67, 19.63, 23.53, 20.24, 20.83, 21.15, 28.47, 19.66, 19.72, 29.27, 17.82, 20.19, 26.54, 26.05, 18.86, 21.07, 21.3, 19.94, 22.04, 18.22, 28.51, 28.52, 20.69, 22.69, 19.16, 19.6, 22.86, 20.22, 20.85, 19.66, 28.46, 32.24, 20.83, 20.57, 19.07, 19.49, 22.39, 21.1, 19.55, 19.58, 29.78, 27.69, 19.37, 18.66, 19.52, 19.6, 19.67, 20.09, 20.24, 22.78, 20.35, 18.53, 29.09, 31.54, 27.21, 19.54, 23.58, 20.85, 19.62, 21.22, 19.61, 24.36, 18.68, 18.71, 33.05, 20.87, 20.97, 19.61, 21.68, 20.25, 21.68, 21.01, 19.64, 28.63, 29.33, 20.95, 19.22, 20.22, 19.53, 19.61, 30.64, 19.67, 24.94, 29.19, 18.73, 19.31, 26.02, 19.16, 19.56, 24.85, 19.22, 20.29, 19.58, 20.14, 18.61, 19.53, 20.28, 18.46, 19.66, 19.61, 24.73, 19.9, 26.23, 20.28, 18.53, 18.7, 19.35, 30.9, 20.86, 21.9, 20.85, 20.32, 31.0, 31.58, 20.53, 19.59, 18.64, 28.33, 19.01, 20.38, 20.41, 20.37, 20.33, 25.67, 29.62, 19.2, 18.54, 29.53, 19.58, 18.71, 16.66, 18.57, 19.5, 20.3, 19.53, 20.76, 21.0, 19.56, 18.91, 19.43, 18.44, 19.34, 18.69, 20.86, 20.82, 20.32, 20.23, 19.61, 19.67, 21.16, 27.57, 21.49, 22.36, 19.42, 20.21, 21.53, 31.51, 20.35, 32.2, 19.09, 23.12, 20.6, 18.58, 20.76, 20.88, 20.1, 23.08, 19.57, 19.64, 26.2, 20.24, 28.82, 32.55, 18.52, 19.46, 21.45, 20.87, 19.6, 20.14, 25.71, 32.29, 19.66, 18.67, 19.65, 32.77, 18.59, 19.28, 20.77, 29.8, 19.52, 18.58, 19.53, 18.65, 28.62, 20.36, 31.16, 19.61, 21.83, 20.79, 27.56, 24.57, 19.69, 25.99, 18.77, 19.32, 20.83, 18.75, 19.7, 20.83, 20.19, 20.86, 36.13, 18.59, 19.51, 20.89, 20.88, 19.7, 28.09, 19.71, 19.86, 20.26, 21.97, 19.69, 18.53, 19.19, 18.68, 20.24, 20.27, 18.98, 18.63, 20.61, 19.84, 22.66, 19.7, 29.13, 18.7, 23.24, 19.04, 20.31, 19.54, 24.49, 20.33, 20.32, 19.64, 19.64, 19.2, 18.68, 16.12, 19.63, 18.6, 17.92, 20.81, 20.07, 21.85, 21.19, 19.16, 19.76, 18.68, 29.13, 20.25, 18.66, 20.7, 19.43, 19.52, 26.8, 18.63, 28.8, 23.91, 17.9, 16.46, 19.65, 19.47, 19.71, 20.72, 19.6, 18.57, 26.87, 18.63, 18.69, 29.15, 27.48, 19.53, 19.75, 26.28, 21.52, 18.48, 18.59, 19.62, 19.64, 19.64, 20.31, 20.28, 20.34, 35.18, 18.32, 20.28, 18.71, 21.43, 18.58, 18.66, 20.76, 19.95, 19.48, 23.49, 20.31, 19.33, 20.13, 19.13, 42.26, 20.31, 29.26, 19.61, 20.83, 24.57, 20.05, 20.26, 29.99, 30.51, 29.76, 18.63, 20.45, 20.31, 20.34, 19.17, 17.61, 18.48, 20.27, 29.36, 30.24, 19.94, 18.7, 20.85, 28.21, 20.36, 29.64, 19.35, 19.73, 36.75, 20.76, 25.89, 19.58, 19.53, 28.3, 19.58, 20.3, 22.47, 19.47, 14.46, 19.38, 19.57, 19.61, 24.62, 34.89, 29.13, 19.57, 19.87, 19.63, 33.84, 20.25, 20.31, 28.91, 21.6, 19.59, 21.93, 20.17, 20.64, 20.37, 19.71, 18.56, 19.65, 20.1, 26.83, 20.76, 19.62, 18.43, 18.71, 29.39, 20.26, 19.61, 20.84, 19.44, 20.85, 18.48, 29.12, 19.48, 20.56, 28.83, 18.32, 25.49, 19.48, 20.26, 20.73, 18.79, 28.43, 20.28, 20.31, 27.31, 19.44, 19.57, 19.46, 20.5, 19.64, 20.12, 20.2, 35.82, 18.59, 19.08, 19.0, 27.98, 18.64, 19.62, 18.03, 18.64, 20.08, 19.63, 29.36, 19.51, 31.58, 19.58, 19.53, 43.67, 20.89, 19.06, 18.61, 31.16, 21.49, 25.4, 37.2, 20.3, 9.82, 19.26, 23.61, 19.49, 22.97, 20.83, 20.63, 20.5, 19.54, 18.78, 19.4, 19.59, 18.01, 29.55, 19.53, 20.18, 21.23, 17.45, 20.75, 20.88, 27.76, 18.64, 19.43, 20.54, 19.88, 20.88, 26.92, 20.76, 20.92, 19.4, 26.2, 28.81, 20.16, 24.53, 20.24, 28.08, 18.62, 20.24, 19.64, 19.59, 33.57, 22.25, 29.07, 20.15, 18.5, 18.6, 26.56, 20.86, 20.17, 21.53, 20.23, 19.49, 20.87, 19.64, 19.63, 20.86, 27.86, 20.83, 19.48, 21.05, 18.44, 18.64, 29.46, 20.95, 28.41, 20.18, 20.21, 19.93, 18.79, 19.36, 20.19, 19.32, 36.76, 18.67, 29.39, 18.69, 20.48, 18.68, 19.32, 27.89, 20.25, 21.88, 20.79, 19.46, 20.34, 28.67, 23.86, 19.64, 24.79, 19.44, 20.14, 21.58, 19.41, 31.44, 20.08, 18.27, 19.52, 25.46, 19.62, 38.63, 27.81, 19.36, 19.39, 31.6, 20.86, 19.53, 18.05, 19.51, 26.0, 20.35, 19.59, 18.22, 25.62, 21.53, 22.49, 29.71, 20.25, 20.82, 21.99, 29.91, 19.1, 19.4, 21.4, 20.28, 20.87, 19.83, 19.68, 30.91, 19.6, 18.44, 20.82, 28.43, 19.65, 20.14, 20.2, 20.29, 30.83, 22.43, 18.36, 29.31, 18.56, 19.32, 21.82, 21.1, 19.49, 18.63, 19.53, 28.88, 28.93, 18.65, 18.68, 19.07, 27.01, 20.13, 20.16, 24.56, 20.83, 19.55, 18.55, 20.33, 29.32, 19.54, 19.71, 27.88, 19.71, 19.66, 20.12, 19.94, 29.38, 35.87, 18.67, 18.83, 19.61, 33.08, 19.59, 21.49, 15.78, 20.7, 18.73, 28.84, 20.2, 30.19, 20.15, 19.58, 19.53, 20.23, 20.31, 19.59, 32.06, 18.64, 18.62, 27.76, 28.55, 20.88, 20.87, 19.58, 20.82, 19.42, 18.65, 18.71, 19.46, 26.19, 19.71, 25.25, 20.19, 21.09, 20.13, 20.74, 19.18, 19.62, 34.32, 24.62, 29.06, 20.84, 20.67, 21.46, 19.71, 20.28, 19.48, 19.51, 19.35, 20.28, 18.62, 18.6, 20.3, 18.56, 31.28, 20.81, 20.32, 18.68, 18.89, 21.52, 18.68, 29.18, 31.45, 20.36, 21.18, 19.14, 18.6, 19.55, 20.27, 20.09, 27.04, 23.53, 22.67, 19.51, 19.38, 28.4, 19.92, 24.53, 20.29, 19.54, 19.66, 20.5, 35.99, 19.62, 26.16, 28.67, 20.33, 19.57, 21.65, 20.16, 19.21, 19.29, 27.08, 20.83, 19.56, 18.67, 19.0, 20.03, 18.69, 20.79, 19.6, 20.3, 19.63, 29.27, 20.21, 19.34, 20.22, 18.68, 19.1, 19.58, 19.91, 20.17, 22.52, 26.16, 20.83, 20.86, 19.54, 27.1, 21.05, 20.28, 22.7, 20.75, 20.22, 21.58, 13.96, 29.3, 19.27, 26.48, 28.73, 31.35, 19.79, 18.7, 19.57, 19.4, 19.64, 25.47, 19.7, 19.53, 24.02, 25.49, 31.0, 22.46, 20.34, 19.45, 20.28, 20.36, 28.67, 20.89, 19.52, 20.21, 21.95, 18.78, 30.84, 19.55, 19.64, 30.34, 17.63, 18.66, 20.32, 28.87, 18.72, 25.17, 19.5, 35.31, 21.56, 20.38, 19.59, 19.65, 19.68, 19.66, 39.62, 18.67, 18.7, 19.48, 20.22, 18.82, 19.45, 22.35, 31.1, 31.33, 28.57, 20.25, 26.68, 33.07, 34.04, 19.65, 19.74, 24.31, 21.56, 19.78, 21.46, 18.52, 25.76, 20.33, 28.98, 19.32, 24.43, 20.27, 19.61, 29.85, 20.75, 19.51, 19.52, 20.23, 19.44, 19.43, 19.55, 19.61, 30.17, 20.22, 20.86, 21.31, 29.31, 30.55, 18.41, 20.29, 20.49, 20.73, 20.32, 19.23, 20.33, 18.9, 24.3, 18.19, 19.23, 18.07, 29.09, 18.68, 34.94, 20.87, 20.27, 20.36, 21.83, 18.82, 19.64, 36.73, 19.52, 18.7, 27.37, 20.23, 19.5, 19.37, 20.27, 20.84, 20.27, 19.61, 31.46, 19.58, 18.57, 20.94, 27.7, 20.81, 19.97, 20.81, 19.48, 29.88, 20.52, 27.01, 18.33, 19.46, 18.71, 18.57, 28.3, 19.62, 19.59, 29.94, 18.64, 23.86, 18.6, 19.51, 19.58, 20.43, 30.31, 30.91, 20.26, 22.14, 29.09, 27.78, 18.72, 24.39, 28.46, 19.64, 33.02, 20.23, 20.8, 20.1, 23.52, 21.73, 19.6, 29.97, 20.68, 28.85, 30.4, 40.1, 19.36, 19.18, 20.77, 30.75, 19.38, 20.28, 26.35, 20.38, 36.2, 24.24, 18.66, 21.05, 19.61, 20.28, 19.54, 20.32, 18.6, 29.59, 18.63, 19.66, 18.9, 21.69, 20.28, 19.67, 18.67, 19.58, 28.2, 29.39, 20.36, 19.51, 18.66, 19.44, 25.28, 29.96, 30.74, 20.67, 27.61, 18.7, 20.33, 20.27, 20.53, 20.29, 20.19, 13.13, 18.63, 19.32, 19.67, 19.85, 19.2, 19.59, 19.4, 30.79, 19.58, 22.01, 23.54, 19.65, 24.8, 26.91, 30.28, 18.99, 25.69, 18.82, 20.56, 20.32, 31.03, 18.48, 16.55, 27.9, 22.92, 18.41, 20.74, 20.74, 19.43, 19.41, 23.19, 20.82, 18.48, 19.3, 19.46, 17.94, 20.95, 20.87, 20.83, 19.43, 20.14, 29.44, 19.55]
    s_y = [9.01, 11.35, 10.1, 10.1, 10.1, 11.35, 11.35, 11.35, 11.35, 11.35, 11.35, 17.17, 14.94, 11.48, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.63, 11.0, 10.51, 21.3, 21.29, 21.27, 21.27, 21.28, 21.27, 21.29, 18.95, 18.89, 14.88, 15.13, 16.07, 16.08, 16.04, 16.04, 16.13, 16.15, 16.15, 13.65, 28.18, 22.72, 23.86, 23.83, 23.83, 24.04, 24.01, 24.0, 23.98, 23.89, 21.45, 25.78, 25.18, 25.2, 25.18, 25.17, 25.17, 25.17, 25.33, 25.21, 25.21, 20.3, 20.3, 21.05, 21.1, 21.13, 21.01, 20.96, 20.93, 20.94, 20.94, 20.82, 22.01, 21.22, 21.78, 21.45, 21.49, 21.88, 21.85, 21.75, 21.93, 21.89, 21.9, 20.98, 20.98, 20.98, 20.98, 21.43, 21.39, 21.38, 21.41, 21.42, 21.26, 21.25, 21.27, 21.26, 21.24, 21.25, 21.22, 20.99, 21.31, 21.24, 21.26, 21.21, 21.4, 21.69, 22.16, 22.14, 22.51, 22.53, 22.51, 22.51, 22.35, 22.34, 22.57, 22.57, 22.75, 22.76, 23.1, 23.1, 23.42, 23.17, 23.15, 23.37, 23.22, 23.23, 23.11, 23.13, 23.12, 23.12, 23.15, 23.12, 22.97, 23.22, 23.06, 23.04, 23.04, 23.21, 22.94, 22.77, 22.76, 22.76, 22.76, 22.76, 22.67, 22.79, 22.8, 22.7, 22.7, 22.51, 22.77, 22.6, 22.49, 22.67, 22.54, 22.52, 22.54, 22.74, 22.71, 23.05, 23.13, 23.14, 23.15, 23.17, 23.07, 22.94, 22.96, 22.96, 22.96, 22.92, 22.92, 22.77, 23.04, 23.27, 23.28, 23.46, 23.31, 23.31, 23.3, 23.3, 23.29, 23.11, 23.48, 23.48, 23.49, 23.48, 23.7, 23.69, 23.75, 23.78, 23.76, 23.96, 23.97, 23.98, 23.82, 23.9, 23.91, 23.85, 23.85, 23.85, 23.98, 23.85, 23.6, 23.85, 23.85, 23.73, 23.59, 23.59, 23.6, 23.48, 23.47, 23.69, 23.71, 23.87, 24.06, 24.14, 24.16, 24.12, 24.09, 24.05, 23.98, 24.18, 24.18, 24.04, 23.88, 23.79, 23.82, 23.82, 23.82, 23.84, 23.72, 23.83, 23.83, 23.66, 23.62, 23.53, 23.39, 23.38, 23.25, 23.25, 23.41, 23.29, 23.28, 23.28, 23.27, 23.53, 23.53, 23.54, 23.54, 23.7, 23.72, 23.66, 23.66, 23.99, 23.84, 24.09, 24.09, 24.09, 24.28, 24.27, 24.27, 24.22, 24.32, 24.75, 24.71, 24.56, 24.54, 24.8, 24.86, 24.86, 24.86, 24.83, 24.71, 24.72, 24.75, 24.54, 24.59, 24.61, 24.45, 24.45, 24.46, 24.46, 24.46, 24.33, 24.34, 24.52, 24.83, 24.83, 24.94, 24.94, 24.95, 25.09, 25.1, 25.11, 25.13, 25.14, 25.23, 25.12, 25.12, 25.03, 25.02, 24.91, 24.93, 24.92, 25.07, 25.29, 25.29, 25.45, 25.44, 25.36, 25.27, 25.37, 25.29, 25.29, 25.17, 25.17, 25.19, 25.37, 25.38, 25.37, 25.26, 25.34, 25.34, 25.34, 25.34, 25.34, 25.41, 25.57, 25.59, 25.68, 25.81, 25.76, 25.76, 25.75, 25.63, 25.62, 25.63, 25.64, 25.7, 25.69, 25.79, 25.8, 25.75, 25.75, 25.75, 25.76, 25.69, 25.79, 25.72, 26.01, 25.8, 25.79, 25.64, 25.43, 25.46, 25.3, 25.29, 25.3, 25.29, 25.44, 25.23, 25.22, 25.23, 25.44, 25.55, 25.55, 25.59, 25.75, 25.74, 25.76, 25.76, 25.73, 25.54, 25.85, 25.84, 25.65, 25.65, 25.86, 25.69, 25.54, 25.55, 25.44, 25.46, 25.65, 25.47, 25.46, 25.35, 25.35, 25.37, 25.21, 25.23, 25.37, 25.47, 25.49, 25.36, 25.36, 25.54, 25.54, 25.56, 25.58, 25.73, 25.7, 25.72, 25.75, 25.84, 25.65, 25.52, 25.52, 25.49, 25.49, 25.8, 25.68, 25.59, 25.72, 25.85, 25.87, 25.89, 25.98, 26.22, 26.18, 26.12, 25.97, 25.97, 25.95, 25.95, 26.09, 26.34, 26.34, 26.34, 26.32, 26.18, 26.19, 26.2, 26.18, 26.19, 26.33, 26.35, 26.22, 26.41, 26.41, 26.34, 26.34, 26.29, 26.29, 26.28, 26.28, 26.28, 26.28, 26.29, 26.13, 26.25, 26.24, 26.25, 26.16, 26.25, 26.26, 26.26, 26.23, 26.24, 26.51, 26.51, 26.52, 26.39, 26.54, 26.4, 26.49, 26.43, 26.33, 26.46, 26.47, 26.47, 26.29, 26.7, 26.7, 26.69, 26.69, 26.59, 26.48, 26.48, 26.6, 26.44, 26.43, 26.57, 26.6, 26.58, 26.58, 26.44, 26.46, 26.44, 26.6, 26.72, 26.59, 26.6, 26.6, 26.61, 26.61, 26.59, 26.61, 26.61, 26.61, 26.73, 26.75, 26.77, 26.77, 26.63, 26.75, 26.64, 26.77, 26.69, 26.69, 26.8, 26.83, 26.84, 26.83, 26.83, 26.85, 26.83, 26.85, 26.83, 26.83, 26.84, 26.91, 26.93, 26.93, 26.93, 26.96, 27.07, 26.97, 26.96, 26.93, 26.86, 26.86, 26.87, 26.87, 26.88, 26.89, 26.89, 26.9, 26.9, 26.96, 26.97, 26.95, 27.02, 27.18, 27.18, 27.18, 27.19, 27.17, 27.17, 27.23, 27.23, 27.2, 27.2, 27.16, 27.24, 27.22, 27.15, 27.16, 27.04, 27.17, 27.1, 27.1, 27.26, 27.24, 27.34, 27.42, 27.39, 27.35, 27.37, 27.36, 27.37, 27.36, 27.56, 27.74, 27.76, 27.76, 27.76, 27.75, 27.75, 27.75, 27.75, 27.81, 27.8, 27.77, 27.71, 27.77, 27.77, 27.77, 27.71, 27.75, 27.74, 27.85, 27.97, 27.95, 27.96, 27.95, 27.95, 27.95, 27.95, 27.9, 27.93, 27.87, 27.9, 27.95, 27.95, 27.94, 27.93, 27.93, 27.88, 27.94, 27.94, 28.0, 27.95, 27.94, 27.87, 27.83, 27.8, 27.8, 27.8, 27.8, 27.81, 27.81, 27.8, 27.79, 27.86, 27.81, 27.83, 27.82, 27.82, 27.83, 27.83, 27.78, 27.7, 27.7, 27.7, 27.79, 27.8, 27.81, 27.9, 27.9, 27.91, 27.9, 27.85, 27.85, 27.92, 27.93, 27.89, 27.93, 27.93, 28.03, 28.03, 28.04, 28.03, 28.03, 28.03, 28.02, 28.03, 28.13, 28.15, 28.16, 28.15, 28.15, 28.16, 28.16, 28.16, 28.16, 28.14, 28.14, 28.14, 28.14, 28.14, 28.14, 28.15, 28.15, 28.15, 28.15, 28.16, 28.19, 28.19, 28.18, 28.18, 28.18, 28.19, 28.2, 28.2, 28.17, 28.2, 28.2, 28.25, 28.25, 28.26, 28.25, 28.3, 28.34, 28.35, 28.35, 28.35, 28.33, 28.35, 28.32, 28.35, 28.39, 28.43, 28.44, 28.39, 28.39, 28.45, 28.44, 28.48, 28.47, 28.53, 28.53, 28.53, 28.53, 28.53, 28.53, 28.54, 28.54, 28.54, 28.51, 28.53, 28.51, 28.56, 28.63, 28.62, 28.62, 28.61, 28.62, 28.62, 28.63, 28.63, 28.62, 28.65, 28.64, 28.65, 28.74, 28.74, 28.74, 28.71, 28.71, 28.71, 28.74, 28.75, 28.75, 28.75, 28.79, 28.77, 28.77, 28.76, 28.77, 28.77, 28.77, 28.77, 28.77, 28.78, 28.78, 28.79, 28.79, 28.79, 28.79, 28.78, 28.79, 28.78, 28.77, 28.75, 28.78, 28.79, 28.79, 28.79, 28.79, 28.77, 28.77, 28.77, 28.77, 28.77, 28.77, 28.78, 28.78, 28.79, 28.78, 28.77, 28.78, 28.77, 28.76, 28.78, 28.77, 28.78, 28.78, 28.78, 28.78, 28.77, 28.77, 28.78, 28.77, 28.77, 28.77, 28.78, 28.79, 28.79, 28.79, 28.81, 28.8, 28.81, 28.81, 28.81, 28.79, 28.81, 28.82, 28.8, 28.81, 28.81, 28.78, 28.79, 28.79, 28.8, 28.81, 28.78, 28.78, 28.82, 28.82, 28.84, 28.84, 28.82, 28.84, 28.84, 28.84, 28.84, 28.82, 28.82, 28.82, 28.82, 28.84, 28.83, 28.82, 28.82, 28.82, 28.82, 28.83, 28.83, 28.82, 28.82, 28.82, 28.82, 28.83, 28.83, 28.81, 28.82, 28.84, 28.84, 28.82, 28.8, 28.8, 28.8, 28.79, 28.83, 28.8, 28.81, 28.81, 28.8, 28.8, 28.82, 28.82, 28.83, 28.83, 28.84, 28.84, 28.83, 28.82, 28.83, 28.83, 28.83, 28.84, 28.83, 28.84, 28.85, 28.84, 28.85, 28.84, 28.83, 28.83, 28.83, 28.83, 28.83, 28.8, 28.74, 28.74, 28.74, 28.74, 28.74, 28.74, 28.76, 28.76, 28.76, 28.76, 28.75, 28.72, 28.72, 28.72, 28.72, 28.72, 28.72, 28.73, 28.73, 28.73, 28.68, 28.63, 28.65, 28.63, 28.63, 28.63, 28.63, 28.63, 28.63, 28.62, 28.6, 28.54, 28.55, 28.45, 28.53, 28.53, 28.54, 28.53, 28.53, 28.44, 28.38, 28.34, 28.34, 28.34, 28.34, 28.34, 28.34, 28.34, 28.36, 28.4, 28.4, 28.4, 28.32, 28.34, 28.31, 28.32, 28.31, 28.34, 28.31, 28.3, 28.32, 28.3, 28.31, 28.29, 28.27, 28.28, 28.27, 28.27, 28.27, 28.27, 28.27, 28.28, 28.23, 28.24, 28.24, 28.2, 28.2, 28.22, 28.26, 28.19, 28.19, 28.19, 28.19, 28.16, 28.11, 28.09, 28.09, 28.08, 28.08, 28.06, 28.0, 27.99, 27.99, 27.98, 27.98, 28.06, 28.01, 28.01, 28.01, 27.95, 27.94, 27.98, 27.97, 27.94, 27.93, 28.07, 28.07, 28.06, 28.12, 28.12, 28.12, 28.08]
    m_y = [7.5, 9.8, 9.58, 15.08, 9.58, 17.75, 15.32, 12.92, 13.94, 14.39, 14.76, 16.28, 16.56, 18.27, 18.15, 18.21, 17.38, 17.23, 17.24, 17.05, 16.99, 14.76, 16.83, 16.84, 16.5, 16.48, 16.28, 16.38, 16.29, 16.24, 16.28, 16.25, 18.15, 18.08, 28.46, 28.16, 32.54, 27.77, 30.49, 30.49, 28.07, 28.03, 27.94, 21.81, 22.35, 32.18, 24.69, 25.74, 27.11, 25.33, 23.33, 23.29, 23.9, 17.96, 23.88, 25.54, 24.41, 24.12, 24.51, 25.11, 26.52, 26.28, 26.32, 26.57, 25.58, 35.05, 31.5, 31.6, 32.37, 32.32, 32.49, 32.48, 32.59, 32.58, 32.53, 45.69, 42.36, 36.75, 38.3, 40.42, 41.1, 41.79, 40.61, 41.96, 42.01, 42.13, 45.07, 44.91, 46.45, 44.21, 45.77, 45.81, 46.33, 46.32, 46.35, 46.56, 46.57, 44.94, 47.7, 46.7, 45.41, 45.43, 44.61, 43.73, 42.32, 42.76, 41.34, 40.8, 38.67, 37.12, 36.94, 35.87, 36.56, 36.7, 37.65, 37.73, 37.51, 37.55, 35.11, 33.16, 34.51, 35.49, 34.41, 34.46, 35.26, 34.3, 33.47, 32.65, 38.63, 34.74, 32.17, 33.85, 34.53, 35.34, 36.19, 36.33, 36.4, 37.09, 35.81, 37.7, 34.6, 35.62, 33.6, 34.92, 35.93, 37.13, 38.12, 39.08, 37.84, 40.1, 40.51, 39.35, 40.2, 39.72, 40.49, 42.8, 42.91, 44.75, 43.86, 41.42, 46.08, 43.27, 44.59, 45.8, 43.84, 42.08, 42.1, 42.23, 42.36, 42.41, 38.67, 35.95, 37.19, 35.49, 36.74, 37.48, 37.71, 38.4, 39.44, 40.39, 40.94, 44.86, 47.83, 49.2, 51.08, 54.91, 57.61, 56.19, 54.24, 56.79, 57.16, 57.76, 53.39, 55.47, 57.44, 58.82, 59.06, 61.06, 61.59, 62.26, 62.95, 62.65, 59.77, 56.73, 57.46, 57.24, 57.05, 56.3, 56.13, 56.1, 55.9, 57.03, 56.84, 56.07, 54.89, 54.49, 54.34, 56.56, 55.8, 55.59, 56.0, 55.7, 55.44, 55.11, 54.36, 54.2, 54.05, 54.14, 53.56, 53.52, 54.54, 54.54, 55.78, 55.85, 55.75, 55.21, 54.28, 62.27, 62.66, 62.75, 63.91, 63.71, 59.89, 59.47, 58.7, 61.95, 63.33, 64.17, 62.94, 64.54, 66.84, 66.32, 66.09, 64.42, 65.82, 65.34, 65.97, 65.34, 64.37, 64.17, 65.15, 63.4, 63.96, 63.97, 63.61, 56.86, 56.48, 56.22, 56.41, 47.53, 47.71, 48.29, 50.29, 51.56, 48.95, 47.06, 47.69, 50.98, 50.3, 50.74, 54.09, 51.56, 52.5, 54.15, 54.51, 63.8, 69.01, 68.83, 69.76, 65.76, 64.53, 64.89, 65.22, 60.7, 60.8, 61.58, 57.87, 56.88, 57.31, 56.69, 57.01, 58.04, 53.74, 53.96, 53.99, 54.14, 54.37, 53.72, 53.23, 54.5, 55.38, 59.56, 59.64, 59.03, 58.44, 58.4, 58.02, 57.88, 58.56, 58.1, 58.68, 58.8, 60.29, 58.64, 58.6, 57.14, 57.83, 58.14, 58.7, 58.65, 58.6, 60.63, 61.37, 64.71, 66.78, 68.09, 65.93, 66.04, 64.76, 62.75, 63.25, 62.69, 64.5, 64.46, 64.19, 64.57, 63.33, 62.07, 61.28, 61.12, 61.51, 60.75, 60.53, 60.39, 60.52, 59.98, 59.87, 56.07, 55.5, 55.26, 58.83, 58.74, 57.86, 57.06, 56.53, 56.67, 57.46, 58.03, 54.5, 55.33, 55.93, 58.28, 59.44, 59.96, 60.82, 60.55, 61.67, 64.02, 64.14, 63.82, 64.82, 65.34, 66.66, 66.27, 57.64, 57.67, 58.29, 58.51, 57.9, 56.29, 58.89, 57.4, 57.64, 58.03, 59.21, 59.42, 59.07, 57.8, 57.12, 57.24, 55.65, 55.49, 54.11, 57.09, 54.22, 55.53, 53.54, 53.8, 54.43, 55.52, 52.77, 52.78, 50.79, 57.0, 53.06, 53.06, 53.06, 52.13, 57.84, 58.51, 60.46, 61.49, 62.23, 60.11, 63.35, 61.87, 61.14, 62.74, 60.34, 61.17, 56.75, 57.77, 59.55, 60.3, 59.99, 60.69, 58.56, 60.84, 63.13, 63.72, 64.14, 63.81, 61.71, 60.43, 60.89, 59.93, 56.33, 57.21, 62.0, 61.31, 60.59, 60.29, 58.66, 59.36, 60.58, 60.22, 60.16, 58.68, 60.81, 59.67, 60.13, 58.31, 58.56, 56.92, 56.81, 57.44, 58.35, 57.09, 57.57, 57.16, 59.93, 61.36, 61.53, 62.03, 61.49, 61.14, 61.64, 62.85, 65.44, 65.59, 65.2, 64.95, 66.4, 66.0, 67.69, 68.05, 69.42, 69.45, 69.08, 69.25, 69.32, 68.22, 68.37, 68.96, 69.58, 69.43, 69.37, 69.94, 70.69, 71.47, 71.62, 71.32, 71.43, 70.59, 70.08, 70.75, 72.5, 72.05, 74.15, 74.99, 74.38, 73.83, 73.51, 72.94, 73.64, 73.98, 75.05, 75.56, 75.62, 75.52, 76.47, 76.02, 75.38, 75.51, 75.55, 75.33, 75.37, 75.5, 76.09, 75.31, 75.86, 76.8, 76.87, 76.73, 76.7, 76.4, 76.1, 75.88, 75.7, 76.98, 76.27, 76.27, 77.28, 78.6, 78.46, 79.85, 78.98, 79.46, 79.43, 80.97, 83.42, 84.21, 83.88, 83.66, 83.65, 82.59, 82.85, 83.12, 83.22, 82.49, 81.68, 80.12, 80.23, 79.07, 77.36, 76.15, 76.48, 76.08, 77.33, 78.47, 77.32, 79.24, 81.15, 80.81, 80.01, 78.85, 79.44, 79.08, 78.26, 78.36, 80.39, 82.05, 83.69, 84.05, 83.15, 82.5, 84.33, 84.76, 84.18, 83.76, 82.79, 82.33, 83.31, 82.96, 81.89, 83.85, 83.4, 82.98, 82.68, 82.99, 82.73, 83.59, 82.73, 80.82, 80.74, 80.9, 81.14, 80.39, 81.66, 81.57, 81.47, 83.62, 83.58, 83.19, 83.31, 82.87, 82.99, 81.32, 80.58, 79.36, 79.7, 79.84, 78.74, 77.79, 77.7, 78.08, 78.28, 77.95, 77.37, 76.63, 76.44, 76.18, 76.27, 75.82, 75.96, 75.5, 74.95, 74.39, 74.73, 75.12, 74.99, 75.04, 75.08, 75.44, 75.22, 75.54, 75.48, 75.17, 75.85, 76.15, 75.39, 74.85, 74.51, 74.39, 73.81, 73.69, 73.26, 73.44, 73.15, 72.69, 72.5, 72.02, 72.69, 72.88, 74.0, 73.37, 73.07, 72.71, 72.74, 72.35, 71.99, 72.45, 72.14, 71.72, 72.74, 74.17, 73.99, 73.87, 75.77, 74.76, 76.41, 75.84, 75.08, 74.81, 74.73, 76.32, 76.04, 76.22, 75.7, 76.54, 75.93, 75.11, 75.51, 75.07, 74.5, 73.82, 73.42, 73.01, 72.62, 72.18, 71.48, 72.31, 72.46, 71.86, 71.68, 71.13, 71.66, 72.1, 72.22, 71.89, 72.04, 71.77, 71.58, 71.61, 71.57, 71.27, 71.09, 71.67, 70.99, 70.79, 70.89, 70.81, 71.11, 70.92, 70.52, 71.42, 72.05, 72.04, 71.73, 71.53, 71.59, 71.55, 71.43, 72.08, 71.85, 72.28, 72.4, 72.2, 72.29, 72.04, 71.8, 71.65, 71.84, 71.41, 71.23, 71.9, 71.74, 72.28, 72.67, 72.49, 72.31, 72.3, 72.53, 72.06, 71.82, 71.73, 72.27, 72.67, 72.38, 73.08, 72.98, 72.78, 72.45, 72.36, 72.36, 72.15, 71.82, 71.63, 71.6, 71.38, 72.23, 72.01, 71.94, 71.92, 71.56, 71.45, 72.48, 73.05, 72.64, 73.41, 73.11, 73.05, 72.55, 72.38, 72.01, 71.91, 71.59, 71.48, 71.21, 70.74, 70.68, 70.58, 71.04, 70.12, 70.11, 69.67, 69.76, 70.34, 70.0, 69.86, 70.77, 70.2, 70.58, 70.37, 69.87, 70.26, 70.28, 70.12, 69.38, 70.58, 70.51, 70.04, 69.87, 70.55, 70.59, 69.76, 70.37, 70.04, 69.53, 69.27, 68.75, 68.77, 69.41, 70.01, 70.05, 70.44, 71.06, 70.58, 70.43, 69.8, 70.11, 69.74, 69.5, 69.72, 70.2, 70.57, 70.37, 69.84, 69.77, 69.63, 69.32, 69.29, 69.28, 69.1, 69.37, 69.23, 68.9, 68.87, 68.16, 67.6, 67.34, 67.34, 66.38, 66.3, 66.94, 67.04, 67.54, 67.92, 67.96, 67.94, 67.7, 67.44, 67.13, 67.4, 67.96, 67.59, 68.06, 68.47, 68.29, 67.95, 67.97, 67.86, 67.75, 68.0, 67.71, 68.14, 67.88, 67.9, 67.68, 68.11, 67.75, 67.66, 67.58, 67.71, 67.65, 67.41, 67.61, 68.33, 68.61, 68.54, 68.15, 67.89, 67.66, 67.85, 67.79, 68.27, 68.65, 68.85, 69.21, 69.25, 69.25, 69.25, 69.1, 69.01, 68.75, 68.61, 68.57, 68.85, 68.93, 69.12, 69.41, 69.55, 69.25, 69.27, 69.35, 69.13, 69.1, 68.78, 69.03, 69.23, 69.02, 69.33, 69.32, 69.34, 69.01, 68.87, 68.58, 68.35, 68.37, 68.02, 68.22, 67.96, 67.96, 67.9, 67.55, 66.89, 67.03, 66.58, 66.57, 67.29, 67.47, 67.27, 67.13, 67.48, 67.44, 66.87, 67.03, 66.91, 67.43, 67.78, 68.06, 67.85, 67.93, 67.96, 67.76, 67.43, 67.12, 67.12, 67.28, 67.13, 67.0, 66.56, 66.44, 66.85, 66.54, 67.02, 66.34, 66.56, 66.5, 66.61, 66.28, 66.08, 66.12, 66.48, 66.16, 66.22, 66.47, 66.35, 66.46, 66.39, 66.19, 66.26, 66.21, 66.02, 66.48, 66.32, 66.61, 65.82, 65.5, 65.66, 65.59, 65.75, 65.72, 65.52, 65.69, 65.88, 66.33, 66.34, 66.52, 66.41]
    plt.plot(x[::10], a_y[::10], ':',label="fedavg")
    plt.plot(x[::10], s_y[::10],'--',label="fedasync")
    plt.plot(x[::10], m_y[::10],'-',label="myfed")
    plt.xticks(range(0, 1000, 100))  # 设置横坐标刻度为给定的年份
    plt.xlabel('epoch')  # 设置横坐标轴标题
    plt.yticks(range(0, 100, 10))
    plt.ylabel('accuracy')
    plt.legend()  # 显示图例，即每条线对应 label 中的内容
    plt.show()