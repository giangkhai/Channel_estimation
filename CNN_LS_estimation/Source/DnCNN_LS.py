import tensorflow as tf
from tensorflow.keras import layers, models

def create_dncnn_model(learning_rate):
    inputs = layers.Input(shape=(2*K, 1))
    x = layers.Conv1D(64, kernel_size=3, padding='same', activation='relu')(inputs)
    for _ in range(15):
        x = layers.Conv1D(64, kernel_size=3, padding='same', activation=None)(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation('relu')(x)

    output_layer = layers.Conv1D(1, kernel_size=3, padding='same', activation=None)(x)

    output_layer = layers.Add()([inputs, output_layer])


    model = models.Model(inputs=inputs, outputs=output_layer, name="dncnn_model")


    model.summary()

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='mean_squared_error')

    return model


cnn_model = create_dncnn_model(learning_rate=1e-4)
