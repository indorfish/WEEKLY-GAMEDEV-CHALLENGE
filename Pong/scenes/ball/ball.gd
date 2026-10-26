extends CharacterBody2D

@export var speed = 100.0
@export var acceleration = Vector2(1.1, 1.09)
func _ready():# Set initial ball velocity
	velocity = Vector2(speed, 1)

func _physics_process(delta):
#The physics for Le bouncing ball
	var collision = move_and_collide(velocity * delta)
	if collision:
		
		velocity = velocity.bounce(collision.get_normal())
		velocity.x *= acceleration.x
		velocity.y *= acceleration.y
		
