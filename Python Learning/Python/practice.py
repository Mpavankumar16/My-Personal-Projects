def walk(steps, currentStep):
    if(currentStep==steps):
        return
    print(currentStep+1)
    return walk(steps, currentStep+1)

walk(10,0)