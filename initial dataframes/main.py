import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt


if __name__ == '__main__':

    df = pd.read_csv('datawhat.csv')
    # print("shape of dataset : ", df.shape)
    # print(df.columns)

    df_slLow = pd.read_csv('datawhatSlowloris.csv')
    df_Bngn = pd.read_csv('datawhatBenign.csv')



    # print("shape of dataset : ", df.shape)
    # print(df.columns)



    # universal_time = np.array(df_slLow['time'])


    # universal_time_Flow = np.array(df['Flow IAT Mean'])


    # iat_benignBwD = np.array(df_Bngn['Bwd IAT Mean'])
    # iat_benignFwD = np.array(df_Bngn['Fwd IAT Mean'])
    # iat_benignFlow = np.array(df_Bngn['Flow IAT Mean'])
    # iat_benignFlowMin = np.array(df_Bngn['Flow IAT Min'])
    # benign_pckts = np.array(df_Bngn['Flow Pkts/s'])



    # iat_slowlorisBwD = np.array(df_slLow['Bwd IAT Mean'])
    # iat_slowlorisFwD = np.array(df_slLow['Fwd IAT Mean'])
    # iat_slowlorisFlow = np.array(df_slLow['Flow IAT Mean'])
    # iat_slowlorisFlowMin = np.array(df_slLow['Flow IAT Min'])
    # slowloris_pckts = np.array(df_slLow['Flow Pkts/s'])
    # pck_sec = np.array(df['Flow Pkts/s'])


    # print(df.shape)
    # print(slowloris_instances.shape)
    # print(benign_instances.shape)



    n1 = 1010
    n2 = 1360

    #timestamp_analog = time[n1:n2]
    # iat_mean = iat_mean[n1:n2]
    # pck_sec = pck_sec[n1:n2]

    cols = df_Bngn.keys()#[21:23]
    print(cols)
    print(len(cols))



    for i in cols:
        plt.plot(np.array(df_slLow['time'])[n1:n2], np.array(df_Bngn[i])[n1:n2], 'b')
        plt.plot(np.array(df_slLow['time'])[n1:n2], np.array(df_slLow[i])[n1:n2], 'r')
        plt.title('Red: Slowloris Incidents        Blue: Benign traffic')
        plt.xlabel('timestamps (sec)')
        plt.ylabel(i)
        plt.show()

















