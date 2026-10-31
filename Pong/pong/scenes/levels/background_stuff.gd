extends Control

@onready var p1_points = $"../paddle"
@onready var p2_points = $"../paddle2"
@onready var p1_scores_label = $HBoxContainer/MarginContainer/p1_scores_label
@onready var p2_scores_label = $HBoxContainer/MarginContainer2/p2_points_label
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	p1_scores_label.set_text(str(p1_points.points))
	p2_scores_label.set_text(str(p2_points.points))
	
