#version 330 core

layout (location = 0) in vec3 in_position;
layout (location = 1) in vec3 in_color;

uniform mat4 matrix_projection;
uniform mat4 matrix_model;
uniform mat4 matrix_view;

out vec3 color;

void main() {
    color = in_color;
    gl_Position = matrix_projection *
                  matrix_model *
                  matrix_view *
                  vec4(in_position, 1.0);
}