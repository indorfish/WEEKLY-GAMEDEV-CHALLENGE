extends CharacterBody2D

const speed = 100.0

func _ready():# Set initial ball velocity
	velocity = Vector2(speed,50)

func _physics_process(delta):
#The pysics for Le bouncing ball
	var collision = move_and_collide(velocity * delta)
	if collision:
		velocity = velocity.bounce(collision.get_normal())
