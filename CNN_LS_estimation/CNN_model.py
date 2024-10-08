import tensorflow as tf
from tensorflow.keras import layers, models, initializers
def create_model(learning_rate):
    inputs = layers.Input(shape=(2*K, 1))  


    x = inputs
    for i in range(10):
        x = layers.Conv1D(5, kernel_size=64, activation='relu', padding='same')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(0.5)(x)

 
    x = layers.Flatten()(x)

   
    output_layer = layers.Dense(2*K, activation='linear', use_bias=False,
                                kernel_initializer='glorot_uniform')(x)
    output_layer = layers.Reshape((2*K, 1))(output_layer)

    model = models.Model(inputs=inputs, outputs=output_layer, name="cnn_model")


    model.summary()

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='mean_squared_error')

    return model


cnn_model = create_model(learning_rate=1e-3 / 2)
