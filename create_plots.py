    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    #Utility to edit the color of plot

    def change_color(color):
        mpl.rcParams['text.color'] = color
        mpl.rcParams['axes.labelcolor'] = color
        mpl.rcParams['axes.edgecolor'] = color
        mpl.rcParams['xtick.color'] = color
        mpl.rcParams['ytick.color'] = color
    change_color("#00002B")

    #Reads the CV
    df=pd.read_excel('data/CV.xlsx',sheet_name="ScientificPublication",header=1,skiprows=0)
    df.date=pd.to_numeric(df.date)
    print(df.info())

    #Masks for selecting only papers or proceedings
    papers_mask=df['status']=="Journal"
    proc_mask=df['status']=="Proceedings"
    preprint_mask=df['status']=='Preprint'

    #Create the dataframes for papers and proceedings
    papers=df[papers_mask]
    proc=df[proc_mask]
    preprints=df[preprint_mask]

    #Count per year
    years=range(2011,2020,1)
    papers_peryear=papers.groupby('date').count().reindex(years, fill_value=0)
    proc_peryear=proc.groupby('date').count().reindex(years, fill_value=0)
    preprint_peryear=preprints.groupby('date').count().reindex(years, fill_value=0)

    #Create the plot
    # plt.bar(years,papers_peryear['id'], label='Journal Papers', color="#C83771")
    # plt.bar(years,proc_peryear['id'], bottom=papers_peryear['id'], label='Proceedings', color="#00002B")
    # plt.bar(years,preprint_peryear['id'], bottom=papers_peryear['id']+proc_peryear['id'], label='Preprints', color="#6c757d")

    plt.bar(years,papers_peryear['id'], label='Journal Papers')
    plt.bar(years,proc_peryear['id'], bottom=papers_peryear['id'], label='Proceedings')
    plt.bar(years,preprint_peryear['id'], bottom=papers_peryear['id']+proc_peryear['id'], label='Preprints')

    plt.colors
    plt.xticks(years)
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend(loc='best',facecolor="white")
    plt.gca().set_aspect(0.8)
    # plt.savefig('papers.png',dpi=120,transparent=True)
    plt.show()