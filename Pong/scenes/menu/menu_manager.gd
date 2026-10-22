extends Node2D

var nodes = []
var selection = 0
var selected: Node
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	print(get_menu_items())

func get_menu_items():
	nodes = get_children()
	for node in nodes:
		if node.is_in_group("menu_item"):
			return nodes

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	
	selected = nodes[selection]
	selected.wobble()
	#Navigate through menu
	if Input.is_action_just_pressed("up"):
		selection -= 1
	if Input.is_action_just_pressed("down"):
		selection += 1
	#select menu
	if Input.is_action_just_pressed("ui_accept"):
		if selection == 0:
			#change_scene_to_file()
			pass
	if selection + 1 > len(nodes):
		selection = 0
	elif selection < 0:
		selection = len(nodes)-1
	
	print(selection)
